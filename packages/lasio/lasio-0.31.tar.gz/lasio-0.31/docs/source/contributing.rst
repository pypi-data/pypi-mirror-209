Contributing to lasio
=========================

lasio is an open source project released under the
MIT License. It has grown over the years through the wonderful work of many 
`contributors <https://github.com/kinverarity1/lasio/graphs/contributors>`__
on GitHub, and through many discussions.

Your help is very welcome! No contribution is too small. You can help with the
documentation, adding example notebooks, posting ideas or feature requests to
GitHub, or by working on the code - or anything else.

Places you can help
----------------------------

* Please don’t hesitate to open a
  `GitHub issue <https://github.com/kinverarity1/lasio/issues/new>`__
  for any problems you are having with lasio, or any ideas for improvements.
  There are templates to guide you in how to file a
  `bug report <https://github.com/kinverarity1/lasio/issues/new?assignees=&labels=bug&template=bug_report.md&title=>`__,
  or a `request for a new feature or improvement <https://github.com/kinverarity1/lasio/issues/new?assignees=&labels=&template=feature_request.md&title=>`__.
  If you are not sure whether your issue fits under these categories, please
  go ahead and `raise <https://github.com/kinverarity1/lasio/issues/new>`__ one anyway!

* Please feel free to contribute suggested changes. The easiest method is to
  fork lasio on GitHub and
  `submit a pull request <https://github.com/kinverarity1/lasio/pulls>`__
  against the "main" branch. Don’t worry about getting all the details right,
  either way it’s still the most convenient way for me or other maintainers to
  see your changes in context.

* Example LAS files: if you have an
  interesting/difficult/silly/standards-challenged LAS file (any version) you
  would be willing to share with me, please do so! Email it to me at
  `kinverarity@hotmail.com <kinverarity@hotmail.com>`__. The more examples we can
  incorporate into lasio’s regression testing, the better. If you have concerns
  about privacy, I’d suggest obfuscating with find-and-replace on various alpha
  (or numeric) characters before sending it on, and/or deleting any sensitive header
  lines.

How to make contributions
-------------------------

Contributions are always welcome to the code, documentation, or example
notebooks. If you are making a contribution, please make sure you are
working off the latest GitHub main branch. You will want to make your contributions
in a branch taken from `main`, and then when you want to share your changes,
you can publish them by "pushing" your branch to your GitHub fork of the lasio
repository, and opening a PR (pull request) here.

First, create a fork of the lasio repository using the GitHub website. Then
clone your fork locally to your computer::

  $ git clone https://github.com/your-username/lasio
  $ cd lasio

Your fork will be called the "origin" repository - you'll need to know this for
when you push/pull changes to and from your computer.

Adding kinverarity1/lasio as "upstream"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now also add the kinverarity1/lasio repository as the "upstream" repository. This is so that
when other people make changes to kinverarity1/lasio, you can "pull" those changes into
your local copy::

  $ git remote add upstream https://github.com/kinverarity1/lasio

To update the `main` branch of the local copy you have of your fork from the "upstream" repository::

  $ git checkout main
  $ git pull upstream main

And to update the GitHub fork from your local copy::

  $ git checkout main
  $ git push origin main

Making sure you have necessary development dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are some additional packages you needing for running unit/regression tests (`pytest`) and
formatting Python code (`black`). You can install these easily by using::

  $ pip install --editable ".[test]"

Making changes to the code
~~~~~~~~~~~~~~~~~~~~~~~~~~

First, start by making sure your local copy is using the latest copy of code from "upstream" main (see above).
Then create a branch - you can call it whatever is meaningful to you. We switch to `main` so that
your changes are relative to the latest copy of the code in `main`::

  $ git checkout main
  $ git checkout -b your-branch-name
  Switched to a new branch 'your-branch-name'

  (your-branch-name) $

Then you can make your changes. To test them, make sure you have an "editable"
installation of lasio in your Python environment. Shift to the root folder
of the repository and run::

  $ pip install -e .

Then to run all the tests::

  $ pytest

Before publishing your changes please make the code is formatted using `black <https://github.com/psf/black>`__::

  $ black .

Then you can push your changes to your fork::

  $ git push origin your-branch-name

And follow the instructions on your fork's GitHub page to open a pull request (PR) for lasio!

Making changes to the documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Just as valuable as changes to the code, are changes or improvements to the
`Sphinx documentation <https://lasio.readthedocs.io/en/latest/>`__! If you would like to help in this regard, you will
need Sphinx and IPython installed::

  $ pip install sphinx IPython sphinx_rtd_theme

Then create a new branch as above. The documentation is written in RestructuredText,
and can be found in the `docs/source` subfolder of the lasio repository. If you
have any changes, you can build a local copy of the HTML repository to test how it
looks. First change into the docs folder::

  $ cd docs

Then run this to generate a local copy of the HTML docs in the `build/html` folder::

  $ make clean
  $ make html

Once you are happy, please publish your branch and open a PR in the same way as above.

Testing
-------

Every time lasio's main branch is updated, automated tests are run using
`GitHub Actions`_ on Python 3.7, 3.8, 3.9 and 3.10 on Ubuntu and Windows.
lasio may work on Python 3.3, 3.4, 3.5, 3.6 but these are not regularly tested.

To run tests yourself:

.. code-block:: console

    $ pip install "lasio[test]"
    $ pytest

.. _GitHub Actions: https://github.com/kinverarity1/lasio/actions/workflows/ci-tests.yml

Comparative benchmarking of performance when reading LAS files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The test file ``tests/test_speed.py`` reads in a large LAS file and is used
to generate the data used in the following benchmark comparisons.

To compare two branches, run and store the benchmark from the first branch e.g.
main and generate the benchmark from the second branch e.g. dev-branch. Then
run the comparison command.

This same basic technique can be used for testing subsquent changes on a branch.

Make benchmark report for first branch:

.. code-block:: console

    $ mkdir ../lasio-benchmarks
    $ git checkout main
    $ pytest tests/test_speed.py --benchmark-autosave --benchmark-storage ../lasio-benchmarks


Make benchmark report for second branch.

.. code-block:: console

    $ git checkout dev-branch
    $ pytest tests/test_speed.py --benchmark-autosave --benchmark-storage ../lasio-benchmarks


List the available benchmark reports.  Their names start with an incremented
number: 0001, 0002, etc, followed by their git commit.

.. code-block:: console

    $ pytest-benchmark  --storage file://../lasio-benchmarks list
    <path>/0001_d39237c38dcbd4255ac61708287c5f012f8f56da_20220630_185722.json
    <path>/0002_ede364ae5cb8aaa2f821fdda017196121e92ffe6_20220630_194028.json
    ...

Compare two benchmark reports. If the terminal is set to display color then the
output will color data green for better performance and red for worse
performance.

.. code-block:: console

    $ pytest-benchmark  --storage file://../lasio-benchmarks compare 0001 0002

    --------------------------------------------------------------------------------------------- benchmark: 2 tests ---------------------------------------------------------------------------------------------
    Name (time in ms)                                Min                 Max                Mean            StdDev              Median               IQR            Outliers     OPS            Rounds  Iterations
    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    test_read_v12_sample_big (0001_d39237c)     149.3796 (1.0)      157.5133 (1.00)     150.8693 (1.00)     2.9515 (1.03)     149.5928 (1.0)      0.7392 (2.43)          1;1  6.6283 (1.00)          7           1
    test_read_v12_sample_big (0002_ede364a)     149.6045 (1.00)     157.3494 (1.0)      150.8314 (1.0)      2.8771 (1.0)      149.7972 (1.00)     0.3038 (1.0)           1;1  6.6299 (1.0)           7           1
    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Publishing a new release
------------------------

1. Ensure you are on main: ``$ git checkout main``
2. Ensure you are using the latest copy of main: ``$ git pull origin main``
3. Check for any local changes to main: ``$ git status`` - test locally and push if necessary.
4. Check that `GitHub Actions Python CI <https://github.com/kinverarity1/lasio/actions/workflows/ci-tests.yml>`__ for main is passing.
5. Find changes since last version release: see `list of commits <https://github.com/kinverarity1/lasio/commits/main>`__.
6. Summarise these changes in ``changelog.rst``.
7. Run the Jupyter Noteook at `docs/Add links to GitHub for all issue and PR refs in changelog.ipynb <docs/Add%20links%20to%20GitHub%20for%20all%20issue%20and%20PR%20refs%20in%20changelog.ipynb>`__ to add hyperlinks for all issue and PR references.
8. Edit the citation file: ``CITATION.cff``
9. Commit with a message e.g. ``Release v0.31``
10. Tag with the same message e.g. ``git tag v0.31``
11. Push to github - first the commit: ``git push origin main --tags``
12. Create a universal wheel: ``python setup.py bdist_wheel --universal``
13. This will put a new wheel file in ``dist/``
14. Also create a source distribution: ``python setup.py sdist``
15. This will put a source distribution archive in ``dist/``
16. Upload all the new distribution release files (wheel and archive) to PyPI: ``twine upload -u USERNAME -p PASSWORD dist/file``
17. Create a new GitHub release via https://github.com/kinverarity1/lasio/releases/new - select the tag
18. Copy the CHANGELOG text in - convert to RST to Markdown quickly by replacing \`# with # and removing \`_
19. Copy the wheel and source distribution archive files into the release page.
20. Publish the release.

That's it.

Email
-----

Please feel free to email me at `kinverarity@hotmail.com
<kinverarity@hotmail.com>`__ with any suggestions, criticisms, questions,
example files.

Code of Conduct
---------------------------

Our Pledge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age,
body size, disability, ethnicity, gender identity and expression, level of
experience, nationality, personal appearance, race, religion, or sexual
identity and orientation.

Our Standards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention
  or advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
  address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

Our Responsibilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

Scope
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This Code of Conduct applies both within project spaces and in public spaces
when an individual is representing the project or its community. Examples of
representing a project or community include using an official project e-mail
address, posting via an official social media account, or acting as an
appointed representative at an online or offline event. Representation of a
project may be further defined and clarified by project maintainers.

Enforcement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported by contacting the project team at kinverarity@hotmail.com. The
project team will review and investigate all complaints, and will respond in a
way that it deems appropriate to the circumstances. The project team is
obliged to maintain confidentiality with regard to the reporter of an
incident. Further details of specific enforcement policies may be posted
separately.

Project maintainers who do not follow or enforce the Code of Conduct in good
faith may face temporary or permanent repercussions as determined by other
members of the project's leadership.

Attribution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This Code of Conduct is adapted from the `Contributor Covenant version 1.4
<https://www.contributor-covenant.org/version/1/4/>`__.
