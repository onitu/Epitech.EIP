#! /usr/bin/env bash

GIT_DEV_SHOWCASE="https://github.com/onitu/onitu.github.io.git"
SVN_EIP_SHOWCASE="https://labeip.epitech.eu/svn/2015/onitu"

DIR_TMP="/tmp"

DIR_DEV_SHOWCASE="onitu_showcase_dev"
DIR_EIP_SHOWCASE="onitu_showcase_eip"

function fatal {
	echo "$@" && exit 1
}

function main {
	cd "$DIR_TMP"

	git clone "$GIT_DEV_SHOWCASE" "$DIR_DEV_SHOWCASE" || fatal "Unable to clone the source repository"
	svn co "$SVN_EIP_SHOWCASE" "$DIR_EIP_SHOWCASE" || fatal "Unable to checkout the eip repository"

	rm -r "${DIR_EIP_SHOWCASE}/www" || fatal "Unable to remove the showcase in the repository"
	cp -r "${DIR_DEV_SHOWCASE}" "${DIR_EIP_SHOWCASE}/www"

	cd "${DIR_EIP_SHOWCASE}/www"
	rm -rf .git README.md LICENSE

	local fa=( $(svn status 2>&1 | egrep '^\?' | egrep -o '[^ \t]+$') )
	for f in "${fa[@]}"; do
		svn add "$f" || fatal "Unable to add file to the showcase repository"
	done

	echo "Please press return and enter a commit message" && read
	svn commit

	rm -rf "$DIR_DEV_SHOWCASE" "$DIR_EIP_SHOWCASE"
}

main "$@"
