from django.contrib import admin
from .models import (
    Employee,
    Attendance,
    Leave,
    Inventory,
    ProductionOrder,
    QualityInspection,
    Machine,
    NXDrawingVault,
    NXPartGenerator,
    NXPartRequest,
    NXGeneratedPart,
    AIPrediction,
    Vendor,
    PurchaseOrder,
    Customer,
    SalesOrder,
)

admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(Leave)
admin.site.register(Inventory)
admin.site.register(ProductionOrder)
admin.site.register(QualityInspection)
admin.site.register(Machine)
admin.site.register(NXDrawingVault)
admin.site.register(NXPartGenerator)
admin.site.register(NXPartRequest)
admin.site.register(NXGeneratedPart)
admin.site.register(AIPrediction)
admin.site.register(Vendor)
admin.site.register(PurchaseOrder)
admin.site.register(Customer)
admin.site.register(SalesOrder)