# Report for Assignment 1 resit

## Project chosen

Name: H2O Wave

URL: https://github.com/AndreiIoanDaraban/wave

Number of lines of code and the tool used to count it: 38445; Lizard by Python

Programming language: Python

## Coverage measurement with existing tool

Tool used to count the total lines of code (Nloc) of the project: Lizard by Python

Tool used to check and verify the coverage of such files: Coverage.py (Unittest)

Below there can be found the coverage report of the files tested (Only test_ui_ext.py and ui.ext.py are relevant). 
These are the final results after test cases have been written to improve the coverage of ui_ext.py.

Name             Stmts        Miss      Branch      BrPart       Cover

--------------------------------------------------

test.py :                 59        37        16         3       33%

test_ui_ext.py :          15         1         4         1       89%

ui_ext.py   :             13         0         8         0      100%

--------------------------------------------------

TOTAL  :                  87        38        28         4       55%



## Coverage improvement

### Individual tests



Function 1:  "def boxes(*args: str) -> str:"
:


Below is the patch to improve the coverage of the function above:



"def test_boxes(self):
        self.assertEqual(boxes('zone1', 'zone2'), json.dumps(('zone1', 'zone2')))
        self.assertEqual(boxes(), json.dumps(()))"

        


Below is the old coverage report that indicates a low coverage percentage:

Name           Stmts            Miss            Cover

-------------------------------

ui_ext.py  :              13         8       38%

-------------------------------

TOTAL  :                  13         8       38%



More insight into the part that was not covered:




"return json.dumps(args)"




Below is the new coverage that shows an improvement in coverage percentage:

Name             Stmts         Miss        Branch        BrPart         Cover

--------------------------------------------------

test.py     :                59        37        16         3       33%

test_ui_ext.py   :           13         1         2         1       87%

ui_ext.py   :                13         6         8         0       43%

--------------------------------------------------

TOTAL  :                     85        44        26         4       42%




The new coverage result for ui_ext.py is 43%, a 5% increase.

The code works with the ui (User Interface). I did a test case that checks for:

  Multiple Arguments Scenario
  No arguments Scenario

The first assertion covers the part of the code where “boxes” receive multiple string arguments and process them into a JSON array. This ensures that the main functionality of combining multiple zones is tested.

The second assertion covers the part of the code where “boxes” receive no arguments, ensuring that it can handle and return an appropriate result (an empty JSON array) even when no zones are specified.

By testing both scenarios, the test_boxes method ensures that the “boxes” function works correctly in typical use cases (multiple zones) and edge cases (no zones). This comprehensive testing approach increases the overall code coverage by verifying that the “boxes” function behaves as expected in different situations.


Function 2: 


"def box(zone: str, order: Optional[int] = None, size: Optional[Union[str, int]] = None, width: Optional[str] = None,
        height: Optional[str] = None) -> str:"


      


Below is the patch made to improve the coverage of the function above:



"def test_box(self):
        # Test with minimal args
        self.assertEqual(box('zone1'), json.dumps({'zone': 'zone1'}))
        # Test with all args
        self.assertEqual(box('zone1', 1, '2', '100px', '200px'), json.dumps({'zone': 'zone1', 'order': 1, 'size': '2', 'width': '100px', 'height': '200px'}))
        # Test with int size
        self.assertEqual(box('zone1', size=3), json.dumps({'zone': 'zone1', 'size': '3'}))
        # Test with invalid size
        with self.assertRaises(ValueError):
            box('zone1', size=3.5)"


            

Below is the old coverage report that indicates a low coverage percentage:

Name           Stmts            Miss            Cover

-------------------------------

ui_ext.py  :              13         8       38%

-------------------------------

TOTAL  :                  13         8       38%

More insight into the part that was not covered:




"if size is not None:
        if not isinstance(size, (int, str)):
            raise ValueError('size must be str or int')
        if isinstance(size, int):
            size = str(size)
    return json.dumps(_clean(dict(zone=zone, order=order, size=size, width=width, height=height)))"


    



Below is the new coverage that shows an improvement in coverage percentage:

Name             Stmts           Miss            Branch            BrPart          Cover

--------------------------------------------------

test.py :                       59        37        16         3       33%

test_ui_ext.py  :               16         1         4         1       90%

ui_ext.py    :                  13         1         8         0       95%

--------------------------------------------------

TOTAL   :                      88        39        28         4       54%


The new coverage result for ui_ext.py is 95%, a 57% increase. 


This code again revolves around the ui_ext.py. The function test_box(self) is designed to cover different scenarios and edge cases of the “box” function. Here are the test cases made to cover that function:



Minimal Arguments
All Arguments
Integer Size Argument
Invalid Size Argument

Minimal Arguments: The function should return a JSON string with only the “zone”  attribute. This ensures that the function handles the case where “size”, “order”, “width”, and “height” are “None”, and thus these attributes are not included in the final JSON string.

All Arguments: The function should return a JSON string that includes all provided attributes. This ensures that the function correctly processes and includes all attributes in the final JSON string when they are provided.

Integer Size Arguments: The function should convert the integer size to a string and include it in the JSON output. This covers the part where the function checks if “size” is an integer and converts it to a string.

Invalid Size Argument: The function should raise a “ValueError” because “size” is neither an integer nor a string. This ensures that the function correctly raises an error when “size” is of an invalid type.


### Overall

Below is the original coverage report of the file ui_ext.py without any modification of the file/additional tests:

Name           Stmts            Miss            Cover

-------------------------------

ui_ext.py  :              13         8       38%

-------------------------------

TOTAL  :                  13         8       38%

Below is the finished coverage report, with the 2 functions added to solidify further and cover the code:

Name             Stmts             Miss           Branch          BrPart          Cover

--------------------------------------------------

test.py :                      59        37        16         3       33%

test_ui_ext.py :               19         1         4         1       91%

ui_ext.py  :                   13         0         8         0      100%

--------------------------------------------------

TOTAL   :                      91        38        28         4       56%

