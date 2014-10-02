# pre-commit.sh
git stash -q --keep-index

FILES_PATTERN='\.(py|js)(\..+)?$'
FORBIDDEN='import\spdb\|console.log'
git diff --cached --name-only | \
    grep -E $FILES_PATTERN | \
    GREP_COLOR='4;5;37;41' xargs grep --color --with-filename -n $FORBIDDEN && echo 'COMMIT REJECTED Found "$FORBIDDEN" references. Please remove them before commiting' && exit 1

git stash pop -q
exit 0
