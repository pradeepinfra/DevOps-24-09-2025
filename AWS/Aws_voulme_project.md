# 🧠 AWS EBS Volume & Snapshot – Manual Project (Oregon Region)

### 🎯 Objective
Learn to **manually create, attach, use, back up, and restore** an Amazon EBS volume on an EC2 instance in **Oregon (`us-west-2`)**.

---

## 🧩 1. Launch an EC2 Instance
1. Go to **AWS Console → EC2 → Instances → Launch instance**
2. Name: `EBS-Demo-Instance`
3. AMI: **Amazon Linux 2 (Free Tier eligible)**
4. Instance type: **t2.micro**
5. Key pair: create or select an existing key (e.g., `oregon-demo-key`)
6. Security group:
   - Allow **SSH (port 22)** from your IP.
7. Click **Launch instance**.
8. After creation:
   - Note **Instance ID**
   - Note **Availability Zone** (e.g., `us-west-2a`)

> ⚠️ Make sure all volumes you create use the **same Availability Zone** as your instance.

---

## 💾 2. Create an EBS Volume
1. Navigate to **EC2 → Elastic Block Store → Volumes**
2. Click **Create volume**
3. Configure:
   - **Size:** 5 GiB  
   - **Type:** gp3  
   - **Availability Zone:** same as EC2 instance (e.g., `us-west-2a`)  
   - **Name tag:** `EBS-Demo-Volume`
4. Click **Create volume**

✅ Volume is now available in Oregon region.

---

## 🔗 3. Attach the EBS Volume to Instance
1. Select your volume in **Volumes**
2. Click **Actions → Attach volume**
3. Choose your **instance**
4. Device name: `/dev/sdf`
5. Click **Attach**

✅ The new disk `/dev/sdf` is attached to your instance.

---

## 🧠 4. Connect to EC2 Instance
Use **EC2 Instance Connect** or SSH via terminal:
```bash
ssh -i oregon-demo-key.pem ec2-user@<Public-IP>
```

---

## 🧱 5. Format & Mount the EBS Volume

### Step 1: List block devices
```bash
lsblk
```

Example output:
```
NAME    MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
xvda    202:0    0    8G  0 disk
└─xvda1 202:1    0    8G  0 part /
xvdf    202:80   0    5G  0 disk
```

- `xvda1` → your root disk mounted at `/`
- `xvdf` → your **new EBS volume**

---

### Step 2: Format the new volume (only once)
```bash
sudo mkfs -t ext4 /dev/xvdf
```

💡 Explanation:
- Creates an **ext4 filesystem** on `/dev/xvdf`.
- Run **only once** on a new, empty volume.
- To check before formatting:
  ```bash
  sudo blkid /dev/xvdf
  ```

---

### Step 3: Create a mount directory
```bash
sudo mkdir /data
```

💡 This directory will be used to access the new volume’s files.

---

### Step 4: Mount the volume
```bash
sudo mount /dev/xvdf /data
```

💡 Now the volume is usable. Anything saved under `/data` is stored on the EBS volume.

---

### Step 5: Check mounted drives
```bash
df -h
```

Example output:
```
Filesystem      Size  Used Avail Use% Mounted on
/dev/xvda1      7.8G  1.2G  6.2G  17% /
/dev/xvdf       4.9G   24K  4.6G   1% /data
```

---

### Step 6: Write a test file
```bash
sudo bash -c 'echo "Hello from Oregon EBS volume!" > /data/test.txt'
```

Alternative safer command:
```bash
echo "Hello from Oregon EBS volume!" | sudo tee /data/test.txt > /dev/null
```

💡 Verify:
```bash
cat /data/test.txt
```

✅ Output:
```
Hello from Oregon EBS volume!
```

---

## 📸 6. Create a Snapshot
1. Go to **EC2 → Elastic Block Store → Volumes**
2. Select `EBS-Demo-Volume`
3. Click **Actions → Create snapshot**
4. Description: `Backup of Oregon EBS volume`
5. Click **Create snapshot**

✅ Go to **Snapshots** to confirm creation.

---

## 🔁 7. Restore from Snapshot
1. Go to **EC2 → Snapshots**
2. Select your snapshot → **Actions → Create volume**
3. Choose:
   - **Availability Zone:** `us-west-2a`
   - **Name:** `Restored-Volume`
4. Click **Create volume**
5. After creation:
   - Select new volume → **Actions → Attach volume**
   - Choose your instance
   - Device name: `/dev/sdg`

### Mount restored volume
```bash
lsblk
sudo mkdir /restore
sudo mount /dev/xvdg /restore
cat /restore/test.txt
```

✅ You’ll see:
```
Hello from Oregon EBS volume!
```

---

## 🧹 8. Clean Up Resources
```bash
sudo umount /data
sudo umount /restore
```

Then in AWS Console:
- Detach and delete both volumes
- Delete snapshot
- Terminate instance

---

## 🧾 9. Understanding Each Command

| Command | Purpose | Notes |
|----------|----------|-------|
| `lsblk` | Lists all block devices | Shows new EBS disk name |
| `sudo mkfs -t ext4 /dev/xvdf` | Formats volume | Run once on new volume |
| `sudo mkdir /data` | Creates mount directory | Needed before mounting |
| `sudo mount /dev/xvdf /data` | Mounts volume | Links volume to directory |
| `df -h` | Displays mounted filesystems | Confirms successful mount |
| `sudo bash -c 'echo ...'` | Writes a test file | Confirms write access |
| `cat /data/test.txt` | Reads file | Verifies data on volume |

---

## ⚙️ 10. (Optional) Make Mount Persistent
```bash
sudo blkid /dev/xvdf
# Output: /dev/xvdf: UUID="abcd-1234" TYPE="ext4"
sudo nano /etc/fstab
# Add:
UUID=abcd-1234  /data  ext4  defaults,nofail  0  2
sudo umount /data
sudo mount -a
df -h
```

✅ The mount now auto-loads after reboot.

---

## 🧩 11. Safe Practices
- Always unmount before detaching:
  ```bash
  sudo sync
  sudo umount /data
  ```
- Verify **Availability Zone** before creating/attaching volumes.
- Use **Tags** for easy identification.
- Delete unused resources to avoid charges.

---

## 🏁 Summary

| Step | Action | Result |
|------|---------|--------|
| 1 | Launch EC2 | Instance ready |
| 2 | Create Volume | 5GB EBS created |
| 3 | Attach Volume | Linked to instance |
| 4 | Format & Mount | Ready to use |
| 5 | Write File | Successful write |
| 6 | Snapshot | Backup created |
| 7 | Restore | Data recovered |
| 8 | Cleanup | No extra charges |

---

**Author:** Infravyom IT Technologies – AWS Training Series  
**Region:** Oregon (`us-west-2`)  
**Last Updated:** October 2025
