#!/bin/bash
set -e

ID=$(openssl rand -hex 4)
TESTID=$ID

echo "Making file at ${sectionname}.$TESTID.ipynb"
echo "------------------------------------------"

make_header(){
cat << EOF > ${sectionname}.ipynb
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "$TESTID",
   "metadata": {},
   "source": [
    "# Atlassian Jira Jupyter Tests: $sectionname\n"
   ]
  },
EOF
}


make_section(){
	ID=$(openssl rand -hex 4)

	cat << EOF >> ${sectionname}.ipynb
	{
	   "cell_type": "code",
	   "execution_count": null,
	   "id": "$ID",
	   "metadata": {},
	   "outputs": [],
	   "source": [$(cat $section |sed -e 's/\(.*\)/"\1\\n",/g')]
	}
EOF
}


close_file(){
cat << EOF >> ${sectionname}.ipynb
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
EOF
echo ${sectionname}.ipynb
}

for section in $(find ./ -name "*.py")
	do
	sectionname=$(echo $section | sed 's/\.\/\///')
	echo "${sectionname}"
	make_header
	make_section
	close_file

done 

