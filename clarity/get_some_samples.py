"""Test some clarity lims api stuff via Scilifelab python wrapper.

Per Lundmark, SNP&SEQ
"""

from genologics.lims import *

#login stuff
from genologics.config import BASEURI, USERNAME, PASSWORD

lims = Lims(BASEURI, USERNAME, PASSWORD)
lims.check_version()

project = Project(lims, id='HOG10')
samples = lims.get_samples(projectlimsid=project.id)

sample_num = lims.get_sample_number(projectlimsid='HOG10')
print "Simple: ", sample_num
print "Via Project obj: ", len(samples)

for mysample in samples:
	print "\nNew sample:\n"	
	for key, value in mysample.udf.items():
		print ' ', key, '=', value


