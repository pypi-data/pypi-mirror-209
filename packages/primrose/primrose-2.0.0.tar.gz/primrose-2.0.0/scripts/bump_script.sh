#!/usr/bin/env bash

push_commit() {
  git remote rm origin
  # Add new "origin" with access token in the git URL for authentication
  echo `git branch`
  echo `git status --porcelain`
  git remote add origin https://$GITHUB_PERSONAL_ACCESS_TOKEN@github.com/ww-tech/primrose.git > /dev/null 2>&1
  git push origin HEAD:$TRAVIS_BRANCH --quiet && git push origin HEAD:$TRAVIS_BRANCH --tags --quiet
}

# use git tag to trigger a build and decide how to increment
current_version=`cat $TRAVIS_BUILD_DIR/.bumpversion.cfg | grep "current_version =" | sed -E s,"^.* = ",,`
echo "current version: $current_version"

if [[ $TRAVIS_EVENT_TYPE != 'pull_request' ]]; then
    if [[ $TRAVIS_BRANCH == *'release'* ]]; then
        if [[ ! $current_version =~ ^(.+dev|.+prod)$ || $BUMP_PART != 'release' ]]; then
            # assume the travis tag is major, minor, or patch to indicate how to increment
            echo "detected current version needs an additional bump before release"
            bump2version $BUMP_PART
        fi
        
        message="[skip travis] Bump version: $current_version -> {new_version}"
        
        echo "bumping release version: $message"
        
        bump2version --allow-dirty --tag --commit --message="$message" release
        push_commit
    fi
else
    echo "on pull request"
    if ! [[ $current_version =~ ^(.+dev|.+prod)$ ]]; then
        # assume we increment by a patch for dev
        echo "not tagging this release - bump and create dev version"
        message="[skip travis] Bump version: $current_version -> {new_version}"
        echo "bumping release version: $message"

        bump2version --allow-dirty --commit --message="$message" patch
        push_commit
    fi
fi
