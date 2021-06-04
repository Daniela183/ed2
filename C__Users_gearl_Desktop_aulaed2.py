#!/usr/bin/env python
# coding: utf-8

# In[60]:


from grafos import Grafo
from grafos import mostrarGrafo


# In[61]:


G = Grafo(direcionado = True)


# In[62]:


G.adicionarVertice("Formosa")
G.adicionarVertice("Brasilia")
G.adicionarVertice("Goiania")
G.adicionarVertice("Sao Paulo")
mostrarGrafo(G)


# In[63]:


for vertice in G.getVertices():
    print(vertice)


# In[64]:


G.removerVertice('Sao Paulo')


# In[65]:


for vertice in G.getVertices():
    print(vertice)


# In[66]:


G.adicionarAresta("Formosa", "Brasilia", 80)
G.adicionarAresta("Formosa", "Goiania", 240)
G.adicionarAresta("Brasilia", "Goiania", 160)


# In[67]:


mostrarGrafo(G)


# In[68]:


import random
def matriz():
    return G()["f%d"% random.randint](G)
  
print('A matriz de adjacência é:\n',('80 0 0'), '\n 0 160 0', '\n 0 0 240')
 


# In[ ]: Daniela





# In[ ]:




