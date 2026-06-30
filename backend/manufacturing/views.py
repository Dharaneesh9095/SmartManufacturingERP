import os

from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, JsonResponse

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *


def home(request):
    return render(request, 'home.html')


def modules(request):  
    return render(request, 'modules.html')


def material_management(request):
    return render(request, 'material_management.html')


def production_control(request):
    return render(request, 'production_control.html')


def quality_assurance(request):
    return render(request, 'quality_assurance.html')


def dashboard_page(request):
    return render(request, 'dashboard.html')


def nx_automation(request):
    return render(request, 'nx_automation.html')


def iot_page(request):
    return render(request, 'iot_dashboard.html')


def ai_recommendation(request):
    return render(request, 'ai_recommendation.html')


def predictive_maintenance(request):
    return render(request, 'predictive_maintenance.html')


def production_analytics(request):
    return render(request, 'production_analytics.html')


def employee_attendance(request):
    return render(request, 'employee_attendance.html')


def inventory_management_page(request):
    return render(request, 'inventory_management.html')


def purchase_management_page(request):
    return render(request, 'purchase_management.html')


def sales_management_page(request):
    return render(request, 'sales_management.html')


def generated_parts_page(request):
    parts = NXGeneratedPart.objects.all().order_by('-id')
    return render(request, 'generated_parts.html', {'parts': parts})


@api_view(['GET'])
def dashboard(request):
    data = {
        "total_employees": Employee.objects.count(),
        "total_attendance": Attendance.objects.count(),
        "total_leaves": Leave.objects.count(),
        "total_inventory": Inventory.objects.count(),
        "total_production_orders": ProductionOrder.objects.count(),
        "total_quality_inspections": QualityInspection.objects.count(),
        "total_machines": Machine.objects.count(),
        "total_nx_drawings": NXDrawingVault.objects.count(),
        "total_nx_parts": NXPartGenerator.objects.count(),
        "total_ai_predictions": AIPrediction.objects.count(),
    }

    return Response(data)


@api_view(['GET'])
def production_dashboard(request):
    data = {
        "total_orders": ProductionOrder.objects.count(),
        "running_orders": ProductionOrder.objects.filter(status__iexact="RUNNING").count(),
        "completed_orders": ProductionOrder.objects.filter(status__iexact="COMPLETED").count(),
        "total_machines": Machine.objects.count(),
        "running_machines": Machine.objects.filter(status__iexact="RUNNING").count(),
    }

    return Response(data)


@api_view(['GET'])
def inventory_dashboard(request):
    total_quantity = 0

    for item in Inventory.objects.all():
        total_quantity += item.quantity

    data = {
        "total_items": Inventory.objects.count(),
        "total_quantity": total_quantity,
        "low_stock_items": Inventory.objects.filter(quantity__lt=20).count(),
    }

    return Response(data)


@api_view(['GET'])
def quality_dashboard(request):
    total_defects = 0

    for item in QualityInspection.objects.all():
        total_defects += item.defect_count

    data = {
        "total_inspections": QualityInspection.objects.count(),
        "total_defects": total_defects,
        "rework_pending": QualityInspection.objects.filter(rework_status__iexact="PENDING").count(),
    }

    return Response(data)


@api_view(['GET'])
def iot_dashboard(request):
    data = {
        "machine_temperature": 45,
        "machine_rpm": 2500,
        "power_consumption": 12.5,
        "machine_status": "RUNNING",
        "machine_health": "Good",
        "production_efficiency": 92,
    }

    return Response(data)


@api_view(['GET'])
def nx_dashboard(request):
    data = {
        "total_requests": NXPartRequest.objects.count(),
        "pending_requests": NXPartRequest.objects.filter(status__iexact="Pending").count(),
        "generated_parts": NXGeneratedPart.objects.count(),
    }

    return Response(data)


@api_view(['GET'])
def purchase_dashboard(request):
    total_value = 0

    for po in PurchaseOrder.objects.all():
        total_value += po.total_cost

    data = {
        "total_purchase_orders": PurchaseOrder.objects.count(),
        "approved_orders": PurchaseOrder.objects.filter(status__iexact="Approved").count(),
        "pending_orders": PurchaseOrder.objects.filter(status__iexact="Pending").count(),
        "total_purchase_value": total_value,
    }

    return Response(data)


@api_view(['GET'])
def sales_dashboard(request):
    total_revenue = 0

    for sale in SalesOrder.objects.all():
        total_revenue += sale.total_amount

    data = {
        "total_customers": Customer.objects.count(),
        "total_sales_orders": SalesOrder.objects.count(),
        "completed_orders": SalesOrder.objects.filter(status__iexact="Completed").count(),
        "pending_orders": SalesOrder.objects.filter(status__iexact="Pending").count(),
        "total_revenue": total_revenue,
    }

    return Response(data)


def get_nx_output_file_response(part, file_name):
    file_path = os.path.join(
        settings.MEDIA_ROOT,
        "nx_outputs",
        file_name
    )

    if os.path.exists(file_path):
        return FileResponse(
            open(file_path, "rb"),
            as_attachment=True,
            filename=file_name
        )

    return JsonResponse({
        "error": "File not found",
        "part_name": part.part_name,
        "file_name": file_name,
        "expected_path": file_path
    }, status=404)


def download_nx_file(request, part_id):
    part = get_object_or_404(NXGeneratedPart, id=part_id)
    return get_nx_output_file_response(part, part.nx_file)


def download_step_file(request, part_id):
    part = get_object_or_404(NXGeneratedPart, id=part_id)
    return get_nx_output_file_response(part, part.step_file)


def download_pdf_file(request, part_id):
    part = get_object_or_404(NXGeneratedPart, id=part_id)
    return get_nx_output_file_response(part, part.pdf_file)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class LeaveViewSet(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class ProductionOrderViewSet(viewsets.ModelViewSet):
    queryset = ProductionOrder.objects.all()
    serializer_class = ProductionOrderSerializer


class QualityInspectionViewSet(viewsets.ModelViewSet):
    queryset = QualityInspection.objects.all()
    serializer_class = QualityInspectionSerializer


class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer


class NXDrawingVaultViewSet(viewsets.ModelViewSet):
    queryset = NXDrawingVault.objects.all()
    serializer_class = NXDrawingVaultSerializer


class NXPartGeneratorViewSet(viewsets.ModelViewSet):
    queryset = NXPartGenerator.objects.all()
    serializer_class = NXPartGeneratorSerializer


class NXPartRequestViewSet(viewsets.ModelViewSet):
    queryset = NXPartRequest.objects.all()
    serializer_class = NXPartRequestSerializer


class NXGeneratedPartViewSet(viewsets.ModelViewSet):
    queryset = NXGeneratedPart.objects.all()
    serializer_class = NXGeneratedPartSerializer


class AIPredictionViewSet(viewsets.ModelViewSet):
    queryset = AIPrediction.objects.all()
    serializer_class = AIPredictionSerializer


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class SalesOrderViewSet(viewsets.ModelViewSet):
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer