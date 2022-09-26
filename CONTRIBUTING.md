# Contribution Guide

First of all, thanks for your interest and for taking the time to contribute! This document shall be your guide throughout the contribution process and will hopefully answer any questions you have.

## Table of Contents

- [Response Times](#response-times)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Enhancements](#suggesting-enhancements)
- [Contributing Changes](#contributing-changes)
    - [Prerequisites](#prerequisites)
    - [Development Environment](#development-environment)
    - [Conventions](#conventions)
        - [General](#general)
        - [Python](#python)
        - [Unix Shell Script](#unix-shell-script)
    - [Testing](#testing)
    - [Pull Request](#pull-request)
- [Code of Conduct](#code-of-conduct)
- [Questions](#questions)

## Response Times

This project has been made available to you without expecting anything in return. As a result, maintenance does not happen on a set schedule. Please keep in mind that the irregular maintenance schedule can lead to significant delays in response times.

## Reporting Bugs

Before reporting a bug, please check if the bug occurs in the latest version. If it does, and if it hasn't already been reported in the [bug tracker][1], feel free to [file a bug report][2].

## Suggesting Enhancements

> **Note:** Simplicity is a core principle of this project. Every enhancement suggestion is carefully evaluated and only accepted if the usefulness of the enhancement greatly outweighs any increase in complexity.

Before suggesting an enhancement, please ensure that the enhancement is not implemented in the latest version. In addition, please ensure that there is no straightforward alternative to achieve the desired outcome. If these conditions are met, and if the enhancement hasn't already been suggested in the [enhancement tracker][3], feel free to [file an enhancement suggestion][4].

## Contributing Changes

### Prerequisites

Before making changes that you plan to contribute, please follow these instructions:

- **Changes related to a [reported bug][1]:** Make sure that the bug has not yet been assigned to anybody (and that nobody has volunteered) and write a comment letting the community know that you have decided to fix the bug.
- **Changes related to an unreported bug:** [File a bug report][2].
- **Changes related to an [already suggested enhancement][3]:** Make sure that the enhancement has not yet been assigned to anybody and write a comment letting the maintainers know that you would like to implement the enhancement. Wait until the enhancement suggestion has been assigned to you.
- **Changes related to a not yet suggested enhancement:** [File an enhancement suggestion][4] and wait until it has been assigned to you.

Following these instructions keeps you (and others) from investing time in changes that would get rejected or are already being worked on.

### Development Environment

This project uses [Vagrant][5] to manage a portable development environment. Simply execute `vagrant up` inside the project's directory to start the setup. Once completed, you can access the development environment with `vagrant ssh`.

### Conventions

#### General

- Code *should* document itself (meaningful naming).
- Code *must* be formatted by executing `vagrant ssh -c /mnt/project/sbin/format` inside the project's directory.

#### Python

- The [general conventions][6] *must* be followed.
- [PEP 8][7] *must* be followed.
- Unless the file is inside the `tests` directory, it *must* have following file header:

    ```python
    """
    SublimeSuperSettings
    https://github.com/TobyGiacometti/SublimeSuperSettings
    Copyright (c) <year> Toby Giacometti and contributors
    Apache License 2.0
    """
    ```

- Names of functions/methods that make modifications *must* read as imperative verb phrases. For example: `print_help`, `fork`.
- Names of functions/methods that don't make modifications and return a non-boolean value *must* read as noun phrases. For example: `id`, `type`.
- Names of functions/methods that don't make modifications and return a boolean value *must* read as [predicate phrases][8]. For example: `is_empty`, `exists`.
- Classes/methods/functions *must* be documented using reStructuredText syntax and following template:

    ```python
    """Summary for class/method/function (if not obvious or description is provided).

    Description for class/method/function (if extended documentation is needed).

    :param type name: Description for method/function parameter (if not obvious).
    :raises type: Description for method/function exception (if exception is thrown).
    :return: Description for method/function return value (if not obvious).
    :rtype: type (if value is returned by method/function)
    """
    ```

#### Unix Shell Script

- The [general conventions][6] *must* be followed.
- Lines longer than 80 characters *should* be avoided.
- Commands *must* be grouped and ordered as follows and groups *must* be separated from each other with an empty line:
    1. Environment checks (check if OS is supported, etc.)
    2. Shell option setting/unsetting
    3. File sourcing
    4. Function definitions
    5. Trap registrations
    6. Common variable assignments
    7. Main logic
- Functions *must* be separated from each other with an empty line.
- Function and variable names *must* use snake case.
- Names of functions that make modifications *must* read as imperative verb phrases. For example: `print_help`, `fork`.
- Names of functions that don't make modifications *must* read as [predicate phrases][8]. For example: `is_empty`, `exists`.
- Functions *must* be documented using Markdown syntax and following template:

    ```sh
    #---
    # Summary for function (if not obvious or description is provided).
    #
    # Description for function (if extended documentation is needed).
    #
    # @param $@ Description for all parameters (if function takes multiple arguments that are all of the same type).
    # @param $<number> Description for a parameter (if not using a description for all parameters).
    # @param... Description for remaining parameters (if function takes multiple trailing arguments that are all of the same type).
    # @stdin Description for STDIN (if used).
    # @stdout Description for STDOUT (if used).
    # @stderr Description for STDERR (if used for non-error output).
    # @fd <number> Description for a non-standard file descriptor.
    # @status Description for all status codes (if documenting each status code separately is suboptimal).
    # @status <number> Description for a non-standard status code (if not using a description for all status codes).
    # @exit (if function calls `exit` outside of error cases)
    func() { :; }
    ```

### Testing

This project uses [UnitTesting][9] to run tests. The tests are stored inside the `tests` directory. Simply execute `vagrant ssh -c /mnt/project/sbin/test` inside the project's directory to run the test suite.

### Pull Request

Before creating a pull request, please follow these instructions:

- Recreate the development environment if `sbin/provision` has been modified.
- Ensure that the instructions in the [Prerequisites][10] and [Conventions][11] sections have been followed.
- Lint the codebase by executing `vagrant ssh -c /mnt/project/sbin/lint` inside the project's directory.
- Update the [test suite][12] and exercise the code you have written.
- Update the [README file][13].
- Update the [changelog][14].

After the pull request has been created, confirm that all [status checks][15] are passing. If you believe that a status check failure is a false positive, comment on the pull request and a maintainer will review the failure.

## Code of Conduct

Please note that this project is released with a [contributer code of conduct][16]. By participating in this project you agree to abide by its terms.

## Questions

Still have questions? No problem! Use the [question tracker][17] to [ask a question][18].

[1]: https://github.com/TobyGiacometti/SublimeSuperSettings/issues?q=is%3Aissue+label%3Abug
[2]: https://github.com/TobyGiacometti/SublimeSuperSettings/issues/new?template=bug.md
[3]: https://github.com/TobyGiacometti/SublimeSuperSettings/issues?q=is%3Aissue+label%3Aenhancement
[4]: https://github.com/TobyGiacometti/SublimeSuperSettings/issues/new?template=enhancement.md
[5]: https://www.vagrantup.com
[6]: #general
[7]: https://www.python.org/dev/peps/pep-0008/
[8]: https://en.wikipedia.org/wiki/Predicate_(grammar)
[9]: https://github.com/SublimeText/UnitTesting
[10]: #prerequisites
[11]: #conventions
[12]: #testing
[13]: README.md
[14]: CHANGELOG.md
[15]: https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-status-checks
[16]: CODE_OF_CONDUCT.md
[17]: https://github.com/TobyGiacometti/SublimeSuperSettings/issues?q=is%3Aissue+label%3Aquestion
[18]: https://github.com/TobyGiacometti/SublimeSuperSettings/issues/new?template=question.md
