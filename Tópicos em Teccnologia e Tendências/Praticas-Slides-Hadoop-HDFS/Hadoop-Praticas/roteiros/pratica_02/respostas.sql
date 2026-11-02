-- 6.1)
select 
    count(*) 
from 
    treinamento_coii.forest_fires_brazil

-- 6.2)
select 
    state,
    count(number) as qtd
from 
    treinamento_coii.forest_fires_brazil 
group by 
    state
order by 
    qtd desc

-- 6.3)
select 
    year,
    count(number) as qtd
from 
    treinamento_coii.forest_fires_brazil 
group by 
    year
order by 
    year asc

-- 6.4)

select 
    state,
    count(number) as qtd
from 
    treinamento_coii.forest_fires_brazil 
where 
    year = 2017
group by 
    state
order by 
    qtd desc
