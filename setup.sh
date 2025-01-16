#!/bin/bash -ex

OWNER_NAME=$1
REPO_NAME=$2
PACKAGE_NAME=$3

if [ -z "$REPO_NAME" ]; then
	echo "Usage: $0 <Repo name>"
	exit 1
fi

if [ -z "$PACKAGE_NAME" ]; then
	echo "Usage: $0 <Package name>"
	exit 1
fi

# $(replace_in_file pattern file)
function replace_in_file() {
	if [ "$(uname)" = 'Darwin' ]; then
		# for MacOS
		sed -i '' -e "$1" "$2"
	else
		# for Linux and Windows
		sed -i'' -e "$1" "$2"
	fi
}

mv src/package_name src/"${PACKAGE_NAME}"

replace_in_file s/repo-name/"${REPO_NAME}"/g src/"${PACKAGE_NAME}"/__init__.py

replace_in_file s/owner-name/"${OWNER_NAME}"/g pyproject.toml
replace_in_file s/owner-name/"${OWNER_NAME}"/g README.md
replace_in_file s/owner-name/"${OWNER_NAME}"/g .github/CODEOWNERS

replace_in_file s/repo-name/"${REPO_NAME}"/g pyproject.toml
replace_in_file s/repo-name/"${REPO_NAME}"/g README.md

replace_in_file s/package_name/"${PACKAGE_NAME}"/g pyproject.toml
replace_in_file s/package_name/"${PACKAGE_NAME}"/g README.md

rm ./setup.sh
rm -rf .venv/
make install

rm -rf .git/
git init
git add .
git commit -m "Initial commit"
