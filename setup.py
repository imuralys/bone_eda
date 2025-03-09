import os
import json
import kaggle

# Kiểm tra và tạo thư mục .kaggle
kaggle_dir = os.path.expanduser('~/.kaggle')
os.makedirs(kaggle_dir, exist_ok=True)

# Tạo config
config = {
    "username": "hiimuralys",
    "key": "75ae8a7c35a113a06341e1c34fc3241a"  # Thay bằng key mới
}

# Lưu config
with open(os.path.join(kaggle_dir, 'kaggle.json'), 'w') as f:
    json.dump(config, f)

# Đặt quyền truy cập
os.chmod(os.path.join(kaggle_dir, 'kaggle.json'), 600)

# Tạo file download_dataset.py
import os
import kaggle

# Tải dataset
kaggle.api.dataset_download_files('thanhngan123/btxrd-data', 
                                 path='data',
                                 unzip=True)