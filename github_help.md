Hi all,

Some of you have wondered how to submit your homework via GitHub. If you are having trouble, please follow the following guide (thanks to a student from Fall 2024 for helping to put this together!)
(Edit: updated with the Troubleshooting section at the bottom.)

### Setting up your GitHub repository

* Create a new Private Repo (from Github website -- please make sure your HW solutions are private!)
* Clone Private Repo
* If you have existing changes, copy and paste them in to your new repository

```
git clone https://github.com/YourUsername/YourPrivateRepo.git
cd YourPrivateRepo
```

You can set it up so that you get changes by `git pull` from the original HW repository:

*   Add the original HW repo as upstream remote

```
git remote add upstream https://github.com/OriginalOwner/OriginalHWRepo.git
git fetch upstream
git pull
```

* Copy in any changes that you made to the code manually.
* Then (after your changes), push everything to make sure all of your changes are published

```
git fetch upstream
git push origin --all
```

### Submitting on Gradescope

Lastly, when it comes to submission time:

- Gradescope should allow you to log in via GitHub and submit your code that way.
- Make sure you check over the files that Gradescope includes to ensure that it has gotten the latest version of all of your changes.

- A similar process should work if you are editing via Codespaces on your private repository.

- If you are editing via Codespaces on the official repository, you will need to download the files to your machine manually before submitting. Make sure you include all of your changes to all three files.

Of course, this is optional, if you prefer you can download the repository to your computer (work locally on it without publishing online) and just upload as a `.zip` file.

### Troubleshooting

If you are having trouble submitting your files on Gradescope or excessive download/upload times, please try deleting hidden folders and then uploading again -- it should reduce the size of your folder considerably. Here is how to do that:

*   copy the files to a new folder
*   to show hidden folders, use `ls -alh` in the terminal or Cmd+Shift+. in Finder
*   remove `.venv`
*   remove `.git`
*   remove `.pytest_cache` and `__pycache__`
*   remove the extra copy of `119-hw1` inside your top-level hw1, if present
*   remove any other hidden files
*   then upload.

Removing the extra files is optional, but could help with download and upload times.

That's it. If you have any trouble submitting or your files aren't showing up, let us know!
