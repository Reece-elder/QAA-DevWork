# Tutorial

Env Vars are used to reuse common information, simplify long strings of data or keep confidental data secure. 

Env vars can be used in GitLab CI (and most CI tools..) in multiple ways, with the two easiest being: 

- Within the .gitlab-ci.yml file
- In the projects settings (within GitLab)

### In file vars

variables:
  GLOBAL_VAR: "All jobs can use this!"

first-job:
  variables:
    LOCAL_VAR: "Only this job can use this.."
  script:
    - echo "$GLOBAL_VAR, $LOCAL_VAR"

### In Settings vars

second-job:
  script:
    - echo "$SUPER_SECRET_KEY - DON'T LOOK ITS SECRET"

## Exercise

Add the following env vars:
- 2x global vars
- 1x local var per job
- 2x in settings secret vars

These should be used in the script stage in the commands, the following MUST be done with some type of var: 
- Adding the version number of the project to the end of a file 
- Setting the git config email via a secret variable
