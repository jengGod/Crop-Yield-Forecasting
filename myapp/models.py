from django.db import models

class Province(models.Model):
    name = models.CharField(max_length=100, unique=True)  # ชื่อจังหวัด
    name_long = models.CharField(max_length=100, null=True, blank=True)  # ชื่อจังหวัดแบบเต็ม
    featurecla = models.CharField(max_length=19, null=True, blank=True)  # ประเภทพื้นที่ เช่น "Admin-1 province"
    scalerank = models.IntegerField(null=True, blank=True)  # อันดับความสำคัญของพื้นที่
    labelrank = models.IntegerField(null=True, blank=True)  # อันดับของป้ายกำกับ
    sovereignt = models.CharField(max_length=32, default="Thailand")  # ประเทศที่อธิปไตย (ค่าเริ่มต้นเป็น "Thailand")
    sov_a3 = models.CharField(max_length=3, default="THA")  # รหัสประเทศ 3 ตัว
    adm0_dif = models.IntegerField(null=True, blank=True)  # ระบุว่าต่างจากขอบเขตประเทศหลักหรือไม่
    level = models.IntegerField(null=True, blank=True)  # ระดับการปกครอง เช่น 1 = จังหวัด
    admin = models.CharField(max_length=32, default="Thailand")  # ประเทศที่บริหารพื้นที่นี้
    subunit = models.CharField(max_length=100, null=True, blank=True)  # หน่วยย่อย เช่น ชื่อจังหวัด
    
    class Meta:
        ordering = ['name']  # เรียงตามชื่อจังหวัด

    def __str__(self):
        return self.name
