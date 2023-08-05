# Databricks notebook source
import setuptools

# COMMAND ----------

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read() 
    
setuptools.setup(
    name="ai_dq_module",
    version="1.1.0",
    author="Himanshu",
    author_email="himanshu.tomar@decisionpoint.in",
    description="data quality rules check",
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['utility'], 
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
    install_requires=['openai'],
    python_requires='>=3.8',
)



