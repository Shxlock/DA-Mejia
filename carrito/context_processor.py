def importe_total_carro(request):
    total=0

    #total+=total
    if request.user.is_authenticated:
        if 'carro' in request.session: 
            for key, value in request.session["carro"].items():   
                total=total+int(value["precio"])
    else:
        total="Debes hacer login"    
    
    return {"importe_total_carro":total}