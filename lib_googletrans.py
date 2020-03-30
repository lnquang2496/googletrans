# Requirement:
# Install googletrans package
# Using pip: pip install googletrans
from googletrans import Translator

# Global variable hold resource
g_ggtrans = None

def ggtrans_init():
    global g_ggtrans
    g_ggtrans = Translator(service_urls=['translate.google.com',])

def ggtrans_deinit():
    global g_ggtrans
    g_ggtrans = None

def ggtrans_translate(text, trans_src='auto', trans_dest='en'):
    global g_ggtrans
    l_result = g_ggtrans.translate(text, trans_dest, trans_src)
    return l_result.text
