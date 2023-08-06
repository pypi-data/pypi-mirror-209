from collections import OrderedDict
import configparser


def pytest_collection_modifyitems(config, items: list):
    config_parser = configparser.ConfigParser()
    config_parser.read(config.inifile)
    if config_parser.has_section('test_execution_sequence'):
        seq = config_parser['test_execution_sequence']
        if 'marker_sequence' in seq.keys():
            test_sequence = [marker.strip() for marker in \
                             seq.get('marker_sequence').split(',')]
            # Here we're going to change the execution sequence of tests.
            # We define the sequence in pytest.ini in section 
            # test_execution_sequence with key marker_sequence with comma
            # separation. Logic is as follows.
            # Logic:
            #    1. We go through the available items
            #    2. We check for the sequence of markers mentioned in pytest.ini
            #    3. If the item is not present in the new sequence_dict, then we
            #        append that to the sequence_dict's sequence for that marker
            #   4. Finally we assign the new sequence back to items
            sequence_dict = OrderedDict()
            _added_tests = []
            for seq in test_sequence:
                sequence_dict.update(
                    {
                        seq: []
                    }
                )
            # Traverse through the test_sequence mentioned in pytest.ini
            for seq in test_sequence:
                # Traverse through every item (test function)
                for item in items:
                    # Check if seq is present in available markers for that item and
                    # not already considered, append that to new sequence we're
                    # creating
                    if seq in [i.name for i in item.iter_markers()]:
                        if seq in sequence_dict.keys():
                            if not item in _added_tests:
                                # Appending to new sequence
                                sequence_dict.get(seq).append(item)
                                _added_tests.append(item)
            new_seq = []
            for key in sequence_dict.keys():
                new_seq += sequence_dict.get(key)
            items[:] = new_seq
