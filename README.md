# API Skeleton

The API Skeleton provides a skeleton API for use with flask API projects.

## Testing

### Running the Tests

All of the acceptance tests are contained within the acceptance-tests folder with the feature files under the features folder and the step-definitions under the steps folder.

If you would like to run all of the acceptance tests then navigate into the acceptance-tests folder and run the following command:

```
./run_tests.sh
```

You can also pass arguments to this command as you would if you were just running cucumber on it's own.

For example you can use the following command to display a cut down version of cucumbers progress when it is running:

```
./run_tests.sh --format progress
```

Or you can use the following to run only the scenarios that have been tagged with whatever tags you specify:

```
/run_tests.sh --tags @USXX
```

### Running Rubocop

Rubocop is ruby gem that will check any ruby code in the repository against the ruby style guide and then provide a report of any offenses.

In order to run Rubocop on the acceptance test code then navigate into the acceptance test folder and run the command:

```
./run_linting.sh
```

If you wish to amend what cops are used, what files are ignored when running Rubocop then you will need to put this in the rubocop.yml file.
