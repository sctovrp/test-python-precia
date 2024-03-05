# test-python-precia

## Relevant files

### /main.py

Main file of the project. It can create a log file but right now is configured to display the output in the console.

### /out/app.log

Log file (output) created by the main file.

To create a new log file, go to `main.py` and uncomment the lines 9 and 10.

Or you can replace the logging configuration to this:

```python
logging.basicConfig(
    format="%(asctime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    level=logging.INFO,
    force=True,
    filename='out/app.log',
    filemode='w'
)

```

You can also rename log file in the line 9.

### /Prueba Dev Python Junior Precia - answers.pdf

Modified file with the answers to the questions.
