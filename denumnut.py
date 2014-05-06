import glob
import sys
import os

length = int(sys.argv[1])

infiles = glob.glob('*.sra')
fastqs = []
gzippers = []

for f in infiles:
    os.system("/home/uqmstan1/Beatson_shared/bin/sra-sdk/2.3.4-2/bin/fastq-dump "+f)
    fastqs.append(f.replace(".sra", ".fastq"))

for fq in fastqs:
    n1 = fq.replace(".fastq", "_1.fastq")
    n2 = fq.replace(".fastq", "_2.fastq")
    gzippers.append(n1)
    gzippers.append(n2)
    with open(fq) as fin, open(n1, 'w') as o1, open(n2, 'w') as o2:
        lines = fin.readlines()
        for i in range(0, len(lines)):
            if (i-1) % 4 == 0:
                h  = lines[i-1].split()[0]
                h1 = h+"/1"
                h2 = h+"/2"
                r1 = lines[i][0:76]
                r2 = lines[i][76:].strip()
                misc = lines[i+1].strip().replace(str(2*length), str(length))
                q1 = lines[i+2][0:76]
                q2 = lines[i+2][76:].strip()
                o1.write(h1+"\n")
                o1.write(r1+"\n")
                o1.write(misc+"\n")
                o1.write(q1+"\n")
                o2.write(h2+"\n")
                o2.write(r2+"\n")
                o2.write(misc+"\n")
                o2.write(q2+"\n")

# Tidy up
for fq in gzippers:
    os.system("gzip "+fq)
for fq in fastqs:
    os.system("rm "+fq)
