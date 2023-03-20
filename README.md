# padrao_projeto_singleton
Estrudos sobre Padrões de Projeto Singleton em Python
 
# Padrão de projeto Singleton

- O padrão de projeto Singleton é um dos padrões de projetos mais simples e conhecidosnomundoda programação.
- O Singleton proporciona uma forma de ter um, e somente um, objeto de determinadotipo,alémde um ponto de acesso 
## objetivos do padrão Singleton
- Garantir que um e somente um objeto de determinada classe seja instanciado;
- Oferecer um ponto de acesso para o objeto que seja global no programa;
- Controlar o acesso concorrente a recursos compartilhados;
## Onde usar o Singleton?
O padrão singleton é usando  em casos como:
- logging (logs) 
- operações de bancos de dados
- spoolers de impressão
- e muitos outros cenários em que seja necessário que haja apenas uma única instância de determinado objeto disponível para toda a aplicação.

## Singleton MonoState

É uma abordagem sigleton, onde tem instâncias diferentes da classe só que com o mesmo estados, as instâncias compartilham esse estado

## Exercícios práticos com Singleton

Exemplo: 

- [Singleton](/exercicio_pratico/exemplo_01.py)
- [Singleton MonoState](/exercicio_pratico/singleton_mono_state.py)
- [Singleton lazy](/exercicio_pratico/singleton_with_lazy.py)
- [Singleton Metaclass 1](/exercicio_pratico/singleton_with_metaclass.py)
- [Singleton Metaclass 2](/exercicio_pratico/singleton_with_metaclass2.py)

## Desvantagem de usar Singleton

Variáveis globais podem ser alteradas por engano em algum lugar e poder ser  usadas em outro lugar na aplicação, gerando erros;
• Variáveis referência podem ser criadas para o mesmo objeto. Como o Singleton cria apenas um objeto, várias referências podem ser criadas neste ponto para o mesmo objeto;
• Todas as classes que são dependentes de variáveis globais acabam se tornando altamente acopladas, pois uma mudança feita por uma classe no dado global poderá exercer umimpactoem outra classe;