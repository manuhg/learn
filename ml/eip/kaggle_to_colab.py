!pip install -U -q kaggle
!mkdir -p ~/.kaggle
!echo '{"username":"{user}","key":"{API key"}' > ~/.kaggle/kaggle.json
!chmod 600 ~/.kaggle/kaggle.json
!kaggle kernels pull manuhg/eipdnn -m