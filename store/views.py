from django.shortcuts import render,redirect,get_object_or_404

from django.views.generic import View

from store.forms import VehicleForm,VehicleUpdateForm

from store.models import Vehicle

from django.db.models import Q

# Create your views here.


class VehicleView(View):
    
    template_name = "vehicle_add.html"
    
    form_class = VehicleForm
    
    def get(self,request,*args,**kwargs):
        
        form_instance = self.form_class()
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        form_data = request.POST
        
        form_instance = self.form_class(form_data,files=request.FILES)
        
        if form_instance.is_valid():
            
            data = form_instance.cleaned_data
            
            print(data)
            
            Vehicle.objects.create(**data)
                
                # name = data.get("name"),
                # varient = data.get("varient"),
                # description = data.get("description"),
                # fuel_type = data.get("fuel_type"),
                # running_km= data.get("running_km"),
                # color = data.get("color"),
                # price = data.get("price"),
                # brand = data.get("brand"),
                # owner_type = data.get("owner_type"),
                
                # another method 
                # Vehicle.objects.create(**data)
                

            
            
            return redirect("vehicle-list")
        
        return render(request,self.template_name,{"form":form_instance})
    
class VehicleListView(View):
    
    template_name = "vehicle_list.html"
    
    def get(self,request,*args,**kwargs):
        
        search_text = request.GET.get("filter")
        
        qs = Vehicle.objects.all()
        
        if search_text:
            
            qs = qs.filter(Q(name__contains=search_text)|Q(fuel_type__contains=search_text))
        
        return render(request,self.template_name,{"data":qs})



class VehicleDetailView(View):
    
    template_name = "vehicle_detail.html"
    
    def get(self,request,*args,**kwargs):
        
       
        
        id=kwargs.get("pk")
        
        qs = get_object_or_404(Vehicle,id=id)
        
        return render(request,self.template_name,{"data":qs})


class VehicleDeleteView(View):
    
    def get(self,request,*args,**kwargs):
        
        id = kwargs.get("pk")

        Vehicle.objects.get(id=id).delete()
        
        return redirect("vehicle-list")
    

# class VehicleUpdateView(View):
    
#     template_name = "vehicle_edit.html"

#     form_class = VehicleForm
    
#     def get(self,request,*args,**kwargs):
        
#         id = kwargs.get("pk")
        
#         vehicle_object = Vehicle.objects.get(id=id)
        
#         data = {
#             "name": vehicle_object.name,
#             "varient":vehicle_object.varient,
#             "decscription":vehicle_object.description,
#             "fuel_type":vehicle_object.fuel_type,
#             "running_km":vehicle_object.running_km,
#             "color":vehicle_object.color,
#             "price":vehicle_object.price,
#             "brand":vehicle_object.brand,
#             "owner_type":vehicle_object.owner_type
#         }
        
        
#         form_instance = self.form_class(initial=data)
        
#         return render(request,self.template_name,{"form":form_instance})
    
#     def post(self,request,*args,**kwargs):
        
#         id = kwargs.get(id)
        
#         form_data = request.POST
        
#         form_instance = self.form_class(form_data,files=request.FILES)
        
#         if form_instance.is_valid():
            
#             data = form_instance.cleaned_data
            
#             Vehicle.objects.filter(id=id).update(**data)
            
#             return redirect("vehicle_list")

#         return render(request,self.template_name,{"form":form_instance})
class VehicleUpdateView(View):
    
    template_name = "vehicle_edit.html"
    
    form_class = VehicleUpdateForm
    
    def get(self,request,*args,**kwargs):
        
        id = kwargs.get("pk")
        
        vehicle_object = get_object_or_404(Vehicle,id=id)

        form_instance = self.form_class(instance=vehicle_object)
        
        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        
        id = kwargs.get("pk")
        
        vehicle_object = get_object_or_404(Vehicle,id=id)

        
        
        form_data = request.POST
        
        form_instance = self.form_class(form_data,files=request.FILES,instance=vehicle_object)
        
        if form_instance.is_valid():
            
            form_instance.save()
            
            return redirect("vehicle-list")
        return(request,self.template_name,{"form":form_instance})
