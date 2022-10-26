# Demo
Go through GitHub Actions slides

# Tutorial
Setup Actions for project
1) Create .github folder in repo
2) `mkdir workflows` and create `main.yaml`
3) Add the following to the main.yaml
```yaml
# Name of your workflow
name: GitHub Demo 
# When does this workflow run (push, fork, label etc)
on: [push]
# What jobs are part of this workflow
jobs:
  # What is the name of the job 
  Actions-Demo: 
    # What runner is this job running on
    runs-on: ubuntu-latest
    # What are we doing as part of this job
    steps:
      # Individual steps, run is simply an sh command
    - run: echo 'Job triggered by ${{github.event_name}}'
    - run: echo 'Running on ${{runner.os}}'
      # Using the inbuilt checkout action https://github.com/actions/checkout https://github.com/actions
    - name: Check out repo
      uses: actions/checkout@v3
      # checkout checks out the repo and stores it here
    - run: ls 
    - run: echo 'Job status is ${{job.status}}'

  # Second job running 
  second-job: 
    runs-on: ubuntu-latest
    steps:
    - run: echo '2nd job'
    - run: pwd
```

Force the workflow by pushing new code

```yaml
env:
  DAY_OF_WEEK: Monday

jobs:
  greeting_job:
    runs-on: ubuntu-latest
    env:
      Greeting: Hello
    steps:
      - name: "Say Hello Mona it's Monday"
        run: echo "$Greeting $First_Name. Today is $DAY_OF_WEEK!"
        env:
          First_Name: Mona
```

```yaml
steps:
  - shell: bash
    env:
      SUPER_SECRET: ${{ secrets.SuperSecret }}
    run: |
      example-command "$SUPER_SECRET"
```

# Exercise
1) Add a workflow CI pipeline to an existing project, the pipeline should checkout the repo, list the contents, list the current location and print out the status of the job
2) Set your workflow to trigger when there is a push on a specific branch AND when a pull request is opened


# Custom Bash Scripts + more commands

## Custom Bash Scripts + commands

1) CI can do more than just echo, add the following commands to the editor: 
    - touch
    - rm
    - mkdir
    - ls 
    - pdw
    - whoami

2) Make a bash script that removes all files ending in:
#/ bin/bash

ls
echo "removing all .js files"
rm *.js
ls
touch newBuild.js

3) Run the script locally (works), get my CI pipeline to run script (doesnt work.. no chmod, but ask for debugging help)

4) Within CI Pipeline add 'chmod +x build.sh'

# Exercise

Add a script for each stage (build, test, deploy) that does atleast 4 different processes out of the following: 
- add new file
- remove files / directories
- make directory
- move files
- prints out the current location
- prints out the current user 
- adds a line of text to an existing file
- simple if else statement using another function 
- prints out all of the files in a repo
- pushes a file to a different repo 
