from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# ------------  Product Details ------------->

class ProductDetails(models.Model):
    productId = models.IntegerField(primary_key=True)
    productName = models.CharField(max_length=500)
    productCode = models.CharField(max_length=500)
    brand = models.CharField(max_length=500)
    category = models.CharField(max_length=100)
    unit = models.CharField(max_length=200)
    warehouse = models.CharField(max_length=200)
    tax = models.CharField(max_length=200)
    skuname = models.CharField(max_length=200)
    skucode = models.CharField(max_length=200)
    mrp = models.FloatField()
    saleprice = models.IntegerField()
    purchaseprice = models.CharField(max_length=200)
    barcode = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return super().__str__()





class ProductCategoryMaster(models.Model):
    productId = models.IntegerField(primary_key=True)
    productName = models.CharField(max_length=500)
    desc = models.CharField(max_length=500)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.productName
    
class TaxMaster(models.Model):
    taxId = models.IntegerField(primary_key=True)
    taxName = models.CharField(max_length=500)
    percentage = models.CharField(max_length=100)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.taxName
    
class BrandMaster(models.Model):
    brandId = models.IntegerField(primary_key=True)
    brandName = models.CharField(max_length=500)
    uploadLogo = models.ImageField(upload_to='images/')
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()
    
class UnitMaster(models.Model):
    unitId = models.IntegerField(primary_key=True)
    unitName = models.CharField(max_length=500)
    baseUnit = models.CharField(max_length=500)
    operatorId = models.IntegerField()
    operatorName = models.CharField(max_length=500)
    operationValue = models.CharField(max_length=500)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return super().__str__()
    
class WareHouseMaster(models.Model):
    warehouseId = models.IntegerField(primary_key=True)
    warehouseName = models.CharField(max_length=500)
    contactPerson = models.CharField(max_length=500)
    mobileNo = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=500)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return super().__str__()
    

# --------------------Supplier ----------------->

class SupplierMaster(models.Model):
    supplierId = models.IntegerField(primary_key=True)
    supplierName = models.CharField(max_length=200)
    contactPerson = models.CharField(max_length=200)
    email = models.EmailField()
    phoneNo = models.CharField(max_length=50)
    mobileNo = models.CharField(max_length=50)
    countryName = models.CharField(max_length=200)
    cityName = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    pincode = models.CharField(max_length=200)
    billingAddress = models.CharField(max_length=200)
    billingCity = models.CharField(max_length=300)
    billingCountry = models.CharField(max_length=200)
    shippingAddress = models.CharField(max_length=200)
    shippingCity = models.CharField(max_length=300)
    shippingCountry = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()

# --------------- Customer Details --------------> 
   
class CustomerMaster(models.Model):
    customerId = models.IntegerField(primary_key=True)
    customerName = models.CharField(max_length=500)
    contactPerson = models.CharField(max_length=500)
    email = models.EmailField()
    mobileNo = models.CharField(max_length=50)
    phoneNo = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    countryName = models.CharField(max_length=500)
    cityName = models.CharField(max_length=500)
    pincode = models.CharField(max_length=500)
    uploadLogo = models.ImageField(upload_to='images/')
    desc = models.CharField(max_length=500)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super().__str__()
    
# -------------------Quatation Master -----------> 
  
class QuatationMaster(models.Model):
    quatationId = models.IntegerField(primary_key=True)
    quatationNo = models.CharField(max_length=500)
    deliveryDate = models.DateField()
    supplierName = models.CharField(max_length=500)
    termCondition = models.CharField(max_length=500)
    notes = models.CharField(max_length=500)
    scanBarCode = models.CharField(max_length=500)
    productId = models.IntegerField()
    productName = models.CharField(max_length=500)
    warehouseName = models.CharField(max_length=500)
    unitId = models.IntegerField()
    unitName = models.CharField(max_length=500)
    price = models.FloatField()
    quantity = models.IntegerField()
    befordisTotal = models.CharField(max_length=500)
    discount = models.FloatField()
    afterdisTotal = models.CharField(max_length=500)
    taxId = models.IntegerField()
    taxName = models.CharField(max_length=500)
    total = models.CharField(max_length=500)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.quatationNo
    
# -----------------Purchase Order Master ------------> 

class PurchaseMaster(models.Model):
    purchaseId = models.IntegerField(primary_key=True)
    purchaseName = models.CharField(max_length=500)
    quatationNo = models.CharField(max_length=500)
    deliveryDate = models.DateField()
    supplierName = models.CharField(max_length=500)
    termCondition = models.CharField(max_length=500)
    notes = models.CharField(max_length=500)
    scanBarCode = models.CharField(max_length=500)
    productName = models.CharField(max_length=500)
    warehouseName = models.CharField(max_length=500)
    unitName = models.CharField(max_length=500)
    price = models.FloatField()
    quantity = models.IntegerField()
    beforeDisTotal = models.CharField(max_length=500)
    discount = models.FloatField()
    afterDisTotal = models.CharField(max_length=500)
    taxName = models.CharField(max_length=500)
    total = models.CharField(max_length=500)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.purchaseName
    
# --------------------- Purchase Order Return Details ------------> 

class PurchaseOrderReturn(models.Model):
    productId = models.IntegerField()
    productName = models.CharField(max_length=500)
    warehouseName = models.CharField(max_length=500)
    unitId = models.IntegerField()
    unitName = models.CharField(max_length=500)
    price = models.FloatField()
    quantity = models.IntegerField()
    returnQuantity = models.IntegerField()
    beforeDisTotal = models.CharField(max_length=500)
    discount = models.FloatField()
    afterDisTotal = models.CharField(max_length=500)
    taxId = models.IntegerField()
    taxName = models.CharField(max_length=500)
    total = models.CharField(max_length=500)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.productName
    
# ------------------- Sales Order Details ---------> 
class SalesOrder(models.Model):
    salesId = models.IntegerField(primary_key=True)
    salesOrderNo = models.CharField(max_length=500)
    orderDate = models.DateField()
    deliveryDate = models.DateField()
    customerName = models.CharField(max_length=500)
    termCondition = models.CharField(max_length=500)
    notes = models.CharField(max_length=500)
    scanBarCode = models.CharField(max_length=500)
    productId = models.IntegerField()
    productName = models.CharField(max_length=500)
    warehouse = models.CharField(max_length=500)
    unit = models.CharField(max_length=500)
    price = models.FloatField()
    quantity = models.IntegerField()
    beforeDisTotal = models.CharField(max_length=500)
    afterDisTotal = models.CharField(max_length=500)
    discount = models.CharField(max_length=500)
    totaldiscount = models.CharField(max_length=500)
    tax = models.CharField(max_length=500)
    totaltax = models.CharField(max_length=500)
    total = models.FloatField()
    grandtotal = models.FloatField()
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.salesOrderNo


class SalesOrderReturn(models.Model):
    salesId = models.IntegerField(primary_key=True)
    supplierId = models.IntegerField()
    supplierName = models.CharField(max_length=500)
    salesOrderNo = models.CharField(max_length=500)
    orderDate = models.DateField()
    deliveryDate = models.DateField()
    customerName = models.CharField(max_length=500)
    returnNote = models.CharField(max_length=500)
    productId = models.IntegerField()
    productName = models.CharField(max_length=500)
    warehouseName = models.CharField(max_length=500)
    unitId = models.IntegerField()
    unitName = models.CharField(max_length=500)
    price = models.FloatField()
    quantity = models.IntegerField()
    returnQuantity = models.IntegerField()
    beforeTotal = models.CharField(max_length=500)
    afterTotal = models.CharField(max_length=500)
    discount = models.FloatField()
    taxId = models.IntegerField()
    taxName = models.CharField(max_length=500)
    total = models.CharField(max_length=500)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.salesOrderNo

# --------------- Inventory -----------> 
   
class Inventory(models.Model):
    baseId = models.IntegerField(primary_key=True)
    baseName = models.CharField(max_length=500)
    stock = models.CharField(max_length=500)
    unitPerPrice = models.CharField(max_length=500)
    warehouseId = models.IntegerField()
    warehouseName = models.CharField(max_length=500)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.baseName
    
# --------------- Permission --------------> 
    
class Permission(models.Model):
    permissionId = models.IntegerField(primary_key=True)
    statistics = models.BooleanField()
    sellingProducts = models.BooleanField()
    reminders = models.BooleanField()
    latestInquiries = models.BooleanField()
    recSalesOrdExpShip = models.BooleanField()
    recPurOrdExpDelivery = models.BooleanField()
    viewProducts = models.BooleanField()
    addProduct = models.BooleanField()
    updateProduct = models.BooleanField()
    deleteProduct = models.BooleanField()
    manageProCat = models.BooleanField()
    manageTax = models.BooleanField()
    manageUnit = models.BooleanField()
    manageBrand = models.BooleanField()
    manageWarehouse = models.BooleanField()
    viewSuppliers = models.BooleanField()
    addSupplier = models.BooleanField()
    updateSupplier = models.BooleanField()
    deleteSupplier = models.BooleanField()
    viewCustomers = models.BooleanField()
    addCustomer = models.BooleanField()
    updateCustomer = models.BooleanField()
    deleteCustomer = models.BooleanField()
    viewInquiries = models.BooleanField()
    addInquiry = models.BooleanField()
    updateInquiry = models.BooleanField()
    deleteInquiry = models.BooleanField()
    manageInqStatus = models.BooleanField()
    manageInqSource = models.BooleanField()
    manageReminders = models.BooleanField()
    viewQuotation = models.BooleanField()
    addQuotation = models.BooleanField()
    updateQuotation = models.BooleanField()
    deleteQuotation = models.BooleanField()
    convertPurOrd = models.BooleanField()
    viewQuotDetails = models.BooleanField()
    generateQuotInvoice = models.BooleanField()
    viewPurOrd = models.BooleanField()
    addPurOrd = models.BooleanField()
    updatePurOrd = models.BooleanField()
    deletePurOrd = models.BooleanField()
    viewPurOrd = models.BooleanField()
    returnPurOrd = models.BooleanField()
    viewPurOrdPayments = models.BooleanField()
    addPurOrdPayment = models.BooleanField()
    deletePurOrdPayment = models.BooleanField()
    generatePurOrdInvoice = models.BooleanField()
    viewSalesOrders = models.BooleanField()
    addSalesOrder = models.BooleanField()
    updateSalesOrder = models.BooleanField()
    deleteSalesOrder = models.BooleanField()
    retViewSalesOrder = models.BooleanField()
    retSalesOrder = models.BooleanField()
    viewSalesOrdPayments = models.BooleanField()
    addSalesOrdPay = models.BooleanField()
    deleteSalesOrdPay = models.BooleanField()
    generateSalesInvoice = models.BooleanField()
    viewInventories = models.BooleanField()
    manageInventory = models.BooleanField()
    viewExpense = models.BooleanField()
    addExpense = models.BooleanField()
    updateExpense = models.BooleanField()
    deleteExpense = models.BooleanField()
    manageExpenseCat = models.BooleanField()
    viewPurOrdRep = models.BooleanField()
    viewSalesOrdRep = models.BooleanField()
    viewPurPayRep = models.BooleanField()
    viewExpRep = models.BooleanField()
    viewSalesOrdPayRep = models.BooleanField()
    viewSalesRep = models.BooleanField()
    viewPurRep = models.BooleanField()
    viewProdPurRep = models.BooleanField()
    viewProSalesRep = models.BooleanField()
    viewStockRep = models.BooleanField()
    viewSupplierPayRep = models.BooleanField()
    viewWarehouseRep = models.BooleanField()
    viewProfit = models.BooleanField()
    viewLossRep = models.BooleanField()
    viewRemiders = models.BooleanField()
    addReminder = models.BooleanField()
    updateReminder = models.BooleanField()
    deleteReminder = models.BooleanField()
    viewRoles = models.BooleanField()
    addRole = models.BooleanField()
    updateRole = models.BooleanField()
    deleteRole = models.BooleanField()
    viewUsers = models.BooleanField()
    addUser = models.BooleanField()
    updateUser = models.BooleanField()
    deleteUser = models.BooleanField()
    resetPassword = models.BooleanField()
    assignUserRoles = models.BooleanField()
    assignUserPermission = models.BooleanField()
    viewOnlineUser = models.BooleanField()
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    


    

