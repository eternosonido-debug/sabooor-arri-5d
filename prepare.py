"""Reconstruct the complete GPL source tree from a pinned upstream and patch.
Usage: python3 prepare.py [destination] [--local-base /path/to/upstream-repository]
"""
from pathlib import Path
import argparse,hashlib,json,subprocess
root=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('destination',nargs='?',default='source');ap.add_argument('--local-base');a=ap.parse_args()
dst=Path(a.destination).resolve();assert not dst.exists(),'Destination must not exist; existing work is never overwritten'
spec=json.loads((root/'upstream.json').read_text());patch=root/'patches/sabooor-community.patch'
assert hashlib.sha256(patch.read_bytes()).hexdigest()==spec['patch_sha256'],'Patch checksum mismatch'
subprocess.run(['git','clone','--no-checkout',a.local_base or spec['url'],str(dst)],check=True)
subprocess.run(['git','checkout','--detach',spec['commit']],cwd=dst,check=True)
subprocess.run(['git','apply','--check',str(patch)],cwd=dst,check=True)
subprocess.run(['git','apply',str(patch)],cwd=dst,check=True)
print('Prepared complete source:',dst,'; upstream',spec['commit'])
