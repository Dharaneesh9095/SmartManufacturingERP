from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from manufacturing import views
from manufacturing.views import (
    EmployeeViewSet,
    AttendanceViewSet,
    LeaveViewSet,
    InventoryViewSet,
    ProductionOrderViewSet,
    QualityInspectionViewSet,
    MachineViewSet,
    NXDrawingVaultViewSet,
    NXPartGeneratorViewSet,
    NXPartRequestViewSet,
    NXGeneratedPartViewSet,
    AIPredictionViewSet,

    VendorViewSet,
    PurchaseOrderViewSet,
    CustomerViewSet,
    SalesOrderViewSet,
)

router = routers.DefaultRouter()

router.register('employees', EmployeeViewSet)
router.register('attendance', AttendanceViewSet)
router.register('leave', LeaveViewSet)
router.register('inventory', InventoryViewSet)
router.register('production', ProductionOrderViewSet)
router.register('quality', QualityInspectionViewSet)
router.register('machines', MachineViewSet)
router.register('nx-drawings', NXDrawingVaultViewSet)
router.register('nx-part-generator', NXPartGeneratorViewSet)
router.register('nx-part-requests', NXPartRequestViewSet)
router.register('nx-generated-parts', NXGeneratedPartViewSet)
router.register('ai-prediction', AIPredictionViewSet)
router.register('vendors', VendorViewSet)
router.register('purchase-orders', PurchaseOrderViewSet)
router.register('customers', CustomerViewSet)
router.register('sales-orders', SalesOrderViewSet)



urlpatterns = [
    path('', views.home),
    path('home/', views.home),
    path('dashboard/', views.dashboard_page),
    path('modules/', views.modules),

    path('material-management/', views.material_management),
    path('production-control/', views.production_control),
    path('quality-assurance/', views.quality_assurance),

    path('nx-automation/', views.nx_automation),
    path('generated-parts/', views.generated_parts_page),
    path('ai-recommendation/', views.ai_recommendation),
    path('iot-dashboard/', views.iot_page),
    path('predictive-maintenance/', views.predictive_maintenance),
    path('production-analytics/', views.production_analytics),
    path('employee-attendance/', views.employee_attendance),
    path('inventory-management/', views.inventory_management_page),
    path('purchase-management/', views.purchase_management_page),
    path('api/purchase-dashboard/', views.purchase_dashboard),
    path('sales-management/', views.sales_management_page),
    path('api/sales-dashboard/', views.sales_dashboard),
    



    path('admin/', admin.site.urls),

    path('api/dashboard/', views.dashboard),
    path('api/production-dashboard/', views.production_dashboard),
    path('api/inventory-dashboard/', views.inventory_dashboard),
    path('api/quality-dashboard/', views.quality_dashboard),
    path('api/iot-dashboard/', views.iot_dashboard),
    path('api/nx-dashboard/', views.nx_dashboard),

    path('download/nx/<int:part_id>/', views.download_nx_file),
    path('download/step/<int:part_id>/', views.download_step_file),
    path('download/pdf/<int:part_id>/', views.download_pdf_file),

    path('api/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)