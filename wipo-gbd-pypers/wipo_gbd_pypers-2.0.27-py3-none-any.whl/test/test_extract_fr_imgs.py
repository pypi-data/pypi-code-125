import unittest
from pypers.steps.fetch.extract.fr.imgs import Images
from pypers.utils.utils import dict_update
from pypers.test import mock_db, mockde_db, mock_logger
from mock import patch, MagicMock
import os
import shutil
import copy


def mock_zipextract(source, dest):
    xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<Transaction xmlns="http://www.wipo.int/standards/XMLSchema/trademarks">
  <TradeMarkTransactionBody>
    <TransactionContentDetails>
    </TransactionContentDetails>
  </TradeMarkTransactionBody>
</Transaction>'''
    jpg_dest = os.path.join(dest, 'jpg1.jpg')
    zip_dest = os.path.join(dest, 'zip1.zip')
    for path in [jpg_dest, zip_dest]:
        with open(path, 'w') as f:
            f.write('toto')
    for i in range(0, 101):
        xml_dest = os.path.join(dest, '12%s.xml' % i)
        with open(xml_dest, 'w') as f:
            f.write(xml_content)


mock_get_value_counter = 0


def mock_get_nodevalue(*args, **kwargs):
    global mock_get_value_counter
    res = '12%s' % mock_get_value_counter
    mock_get_value_counter += 1
    return res


class TestMerge(unittest.TestCase):

    path_test = os.path.join(os.path.dirname(__file__), 'foo')
    cfg = {
        'step_class': ' pypers.steps.fetch.extract.fr.imgs.Images',
        'sys_path': None,
        'name': 'Images',
        'meta': {
            'job': {},
            'pipeline': {
                'input': {
                    'from_web': {
                        'credentials': {
                            'user': 'toto',
                            'password': 'password'
                        }
                    }

                },
                'run_id': 1,
                'log_dir': path_test
            },
            'step': {},
        },
        'output_dir': path_test
    }

    extended_cfg = {
        'input_archive': [os.path.join(path_test, 'toto.zip'),
                          os.path.join(path_test, 'toto.tar')],
        'img_ref_dir': path_test
    }

    @patch("pypers.core.interfaces.db.get_db_logger", MagicMock(side_effect=mock_logger))
    def setUp(self):
        try:
            shutil.rmtree(self.path_test)
        except Exception as e:
            pass
        os.makedirs(self.path_test)
        for fin in self.extended_cfg['input_archive']:
            with open(fin, 'w') as f:
                f.write('toto')

        self.cfg = dict_update(self.cfg, self.extended_cfg)

    @patch("pypers.core.interfaces.db.get_db_logger", MagicMock(side_effect=mock_logger))
    def tearDown(self):
        try:
            shutil.rmtree(self.path_test)
            pass
        except Exception as e:
            pass

    @patch('pypers.utils.utils.zipextract',
           MagicMock(side_effect=mock_zipextract))
    @patch('pypers.utils.utils.tarextract',
           MagicMock(side_effect=mock_zipextract))
    @patch("pypers.core.interfaces.db.get_db", MagicMock(side_effect=mock_db))
    @patch("pypers.core.interfaces.db.get_db_logger", MagicMock(side_effect=mock_logger))
    def test_process(self):
        mockde_db.update(self.cfg)
        step = Images.load_step("test", "test", "step")
        step.process()

    @patch("pypers.core.interfaces.db.get_db", MagicMock(side_effect=mock_db))
    @patch("pypers.core.interfaces.db.get_db_logger", MagicMock(side_effect=mock_logger))
    def test_process_2(self):
        tmp = copy.deepcopy(self.cfg)
        mockde_db.update(tmp)
        tmp['input_archive'] = ['foo.txt']
        step = Images.load_step("test", "test", "step")
        try:
            step.process()
            self.fail()
        except Exception as e:
            pass


if __name__ == "__main__":
    unittest.main()
