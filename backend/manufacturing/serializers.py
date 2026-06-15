from rest_framework import serializers
from .models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'


class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'


class ProductionOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionOrder
        fields = '__all__'


class QualityInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityInspection
        fields = '__all__'


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'


class NXDrawingVaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = NXDrawingVault
        fields = '__all__'


class NXPartGeneratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = NXPartGenerator
        fields = '__all__'


class AIPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIPrediction
        fields = '__all__'


class NXPartRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = NXPartRequest
        fields = '__all__'

class NXGeneratedPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = NXGeneratedPart
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class SalesOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrder
        fields = '__all__'

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'