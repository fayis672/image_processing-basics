#!/bin/bash
echo "Enter fearture name:"
read feature_name
echo "$feature_name"
cd image_filters
mkdir -p "$feature_name"
touch "$feature_name/$feature_name.ipynb" 
touch "$feature_name/$feature_name.py"   
