from django.db import models


class Employee(models.Model):
    employee_code = models.CharField(max_length=50, unique=True, default="EMP001")
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    salary = models.FloatField(default=0)
    qr_code = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.qr_code:
            self.qr_code = self.employee_code
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    check_in_time = models.TimeField(auto_now_add=True)
    check_out_time = models.TimeField(blank=True, null=True)
    status = models.CharField(max_length=20, default="Present")
    scan_method = models.CharField(max_length=50, default="QR Scan")

    def __str__(self):
        return f"{self.employee.name} - {self.status}"


class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50)
    reason = models.TextField()
    status = models.CharField(max_length=30, default="Pending")

    def __str__(self):
        return f"{self.employee.name} - {self.leave_type}"


class Inventory(models.Model):
    material_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    vendor_name = models.CharField(max_length=100)
    stock_type = models.CharField(max_length=50)

    def __str__(self):
        return self.material_name


class ProductionOrder(models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    machine_name = models.CharField(max_length=100)
    shift = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.product_name


class QualityInspection(models.Model):
    product_name = models.CharField(max_length=100)
    defect_count = models.IntegerField(default=0)
    rework_status = models.CharField(max_length=50)
    remarks = models.TextField()

    def __str__(self):
        return self.product_name


class Machine(models.Model):
    machine_code = models.CharField(max_length=50, unique=True)
    machine_name = models.CharField(max_length=100)
    machine_type = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    current_output = models.IntegerField(default=0)

    def __str__(self):
        return self.machine_name


class NXDrawingVault(models.Model):
    drawing_name = models.CharField(max_length=100)
    version = models.CharField(max_length=20)
    file = models.FileField(upload_to="nx_drawings/")
    approval_status = models.CharField(max_length=50)

    def __str__(self):
        return self.drawing_name


class NXPartGenerator(models.Model):
    part_name = models.CharField(max_length=100)
    bolt_diameter = models.FloatField()
    bolt_length = models.FloatField()
    material = models.CharField(max_length=100)
    output_type = models.CharField(
        max_length=100,
        default="NX 3D Model, PDF, STEP"
    )

    def __str__(self):
        return self.part_name


class NXPartRequest(models.Model):
    part_name = models.CharField(max_length=100)
    diameter = models.FloatField()
    length = models.FloatField()
    material = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.part_name


class AIPrediction(models.Model):
    production_delay = models.CharField(max_length=100)
    material_shortage = models.CharField(max_length=100)
    machine_downtime = models.CharField(max_length=100)

    def __str__(self):
        return "AI Prediction"


class NXGeneratedPart(models.Model):
    part_name = models.CharField(max_length=100)
    nx_file = models.CharField(max_length=255)
    step_file = models.CharField(max_length=255)
    pdf_file = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.part_name


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    material_supplied = models.CharField(max_length=100)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.vendor_name


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    material_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit_price = models.FloatField()
    total_cost = models.FloatField(default=0)
    status = models.CharField(max_length=50, default="Pending")
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_cost = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.po_number


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_name


class SalesOrder(models.Model):
    so_number = models.CharField(max_length=50, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    selling_price = models.FloatField()
    total_amount = models.FloatField(default=0)
    status = models.CharField(max_length=50, default="Pending")
    created_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_amount = self.quantity * self.selling_price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.so_number


class Warehouse(models.Model):
    warehouse_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()
    utilized_space = models.IntegerField(default=0)

    def __str__(self):
        return self.warehouse_name