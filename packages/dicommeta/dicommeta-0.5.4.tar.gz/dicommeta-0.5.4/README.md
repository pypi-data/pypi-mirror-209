# DicomMeta

dicommeta is a Python library for efficiently storing large amounts of Dicom Metadata

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dicommeta.

```bash
pip install dicommeta
```

## Usage

```python
from pprint import pprint
from src.dicommeta import (Series, Study, Instance)
from dicommeta.Utils import Mode

new_dicom_study = Study(
    StudyInstanceUID='1.3.6.1.4.1.14519.5.2.1.4334.1501.757929841898426427124434115918',
    SpecificCharacterSet='ISO_IR 100',
    StudyDate="20190701",
    StudyTime='023750',
    AccessionNumber='sdfk324234',
    ReferringPhysicianName='Dr Strange',
    PatientName='John Doe',
    PatientID='A123',
    StudyUID='study001',
    PatientBirthDate='2000-01-01',
    mode=Mode.CT)

new_series01 = Series(seriesUID='series001')
new_series01.add_instance(Instance(SOPinstanceUID='Instance001'))
new_series01.add_instance(Instance(SOPinstanceUID='Instance002'))
new_series01.add_instance(Instance(SOPinstanceUID='Instance002'))
new_dicom_study.add_series(new_series01)
new_series11 = Series(seriesUID='series001')
new_series11.add_instance(Instance(SOPinstanceUID='Instance002'))
new_dicom_study.add_series(new_series11)
new_series11.add_instance(Instance(SOPinstanceUID='Instance003'))
new_dicom_study.add_series(new_series11)

new_series02 = Series(seriesUID='series002')
new_series02.add_instance(Instance(SOPinstanceUID='Instance002'))
new_series02.add_instance(Instance(SOPinstanceUID='Instance003'))
new_dicom_study.add_series(new_series02)

pprint(new_dicom_study.get_dict())
pprint(new_dicom_study.get_series(seriesUID='series002'))

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)