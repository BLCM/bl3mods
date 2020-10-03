#!/bin/bash
# vim: set expandtab tabstop=4 shiftwidth=4:

CUR_DIR=$(pwd)

for dir in basegame/*
do
    echo $dir
    cd $dir
    ${CUR_DIR}/process_challenges.py >> ${CUR_DIR}/challenges.py
    cd ${CUR_DIR}
done

for dir in dlc1/*
do
    echo $dir
    cd $dir
    ${CUR_DIR}/process_challenges.py >> ${CUR_DIR}/challenges-dlc1.py
    cd ${CUR_DIR}
done

for dir in dlc2/*
do
    echo $dir
    cd $dir
    ${CUR_DIR}/process_challenges.py >> ${CUR_DIR}/challenges-dlc2.py
    cd ${CUR_DIR}
done

for dir in dlc3/*
do
    echo $dir
    cd $dir
    ${CUR_DIR}/process_challenges.py >> ${CUR_DIR}/challenges-dlc3.py
    cd ${CUR_DIR}
done
