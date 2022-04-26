import streamlit as st
import pandas as pd

################################
from . import emma



##################################

# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()
