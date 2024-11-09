from django import forms

from store.models import Vehicle



class VehicleForm(forms.Form):
    
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    varient = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    description = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    fuel_type = forms.ChoiceField(choices=Vehicle.fuel_options,widget=forms.Select(attrs={"class":"form-control form-select"}))
    
    running_km = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
    
    color = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    price = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))

    brand = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    owner_type = forms.ChoiceField(choices=Vehicle.owner_options,widget=forms.Select(attrs={"class":"form-control form-select"}))
    
    picture = forms.FileField()
    
    
class VehicleUpdateForm(forms.ModelForm):
    
    class Meta:
        
        model = Vehicle
        
        fields = "__all__"
        
        widgets ={
            
            "name" :forms.TextInput(attrs={"class":"form-control"}),
            "fuel_type":forms.Select(attrs={"class":"form-control form-select"}),
            "running_km":forms.NumberInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control","rows":5}),
            "varient":forms.TextInput(attrs={"class":"form-control"}),
            "color":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "owner_type":forms.Select(attrs={"class":"form-control form-select"}),
            "brand":forms.TextInput(attrs={"class":"form-control"}),
            "picture":forms.FileInput(attrs={"class":"form-control"}),
        
            
                
            
            
       
        }

    

    