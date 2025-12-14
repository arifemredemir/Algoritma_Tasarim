#RB-INSERT GENİŞLETİLMİŞ PSEUDO CODE


#GLOBAL SOLA-DONDÜR FONKSIYONU

def SOLA-DONDÜR(T,x): #Durum-2 Fonskiyon Tanımla
					
    y <- right[x]
    right[x] <- left[y]

    if left[y] != NIL

        then
            left[p[y]] <- x
    
    p[y] <- p[x]
    
    if p[x] == NIL

        then root[T] <- y 

    else if x == left[p[x]]
    
        then left[p[x]] <- y 
    
    else 
    
        then right[p[x]] <- y 
             left[y] <- x
             p[x] <- y 



# GLOBAL SAGA-DÖNDÜR FONKSIYONU

def SAGA-DÖNDÜR(T,x): # Durum - 3 Fonksiyon Tanımı
                        
    y <- left[x]

    left[x] <- right[y]

    if right[y] != NIL: 
        
        then right[p[y]] <- x 
      
    p[y] <- p[x]

    if p[x] == NIL: 
        
        then root[T] <- y

    else if x == right[p[x]]:
        
        then right[p[x]] <- y
        
    else: 
        
        then left[p[x]] <- y 
        

    right[y] <- x
    p[x] <- y


#RB-INSERT FONKSIYONU

RB-INSERT(T,x)
	TREE-INSERT(T,x)
	color[x] <- RED   
	
	while x != root[T] and color[p[x]] = RED: 
	
		do if p[x] == left[p[p[x]]]:  
		
			then y <- right[p[p[x]]] 
			
			if color[y] == RED:    #Durum-1 Uygula
			
				then 
				    color[p[x]] <- BLACK
					color[y] <- BLACK
					color[p[p[x]]] <- RED
					x <- p[p[x]]
			
			
			else if x == right[p[x]]  # Durum-2 Kontrolü
			
				then
					x <- p[x]
						    
                    SOLA-DONDÜR(T,x) #Durum-2 Uygula
                    
                color[p[x]] <- BLACK
                color[p[p[x]]] <- RED
                    
                SAGA-DÖNDÜR(T,p[p[x]]) # Durum-3 Uygula
                    
            
            else:

                then 
                    y <- left[p[p[x]]]
                    
                    if color[y] == RED
                    
                        then
                            color[p[x]] <- BLACK
                            color[y] <- BLACK
                            
                            color[p[p[x]]] <- RED
                            
                            x <- p[p[x]]
                    
                    else if x <- left[p[x]]
                    
                            then
                                x <- p[x]
                                
                                SAGA-DÖNDÜR(T,x)
                                
                                color[p[x]] <- BLACK
                                color[p[p[x]]] <- RED
                                
                                SOLA-DONDÜR(T,x)
                                
    color[root[T]] <- BLACK
                   
                            
                    
                        
 
                    
                    
					
					
					
					



			
	


