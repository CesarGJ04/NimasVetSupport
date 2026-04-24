CREATE OR REPLACE VIEW public.vw_unidades_produccion
 AS
 SELECT cp.id,
    cz.name AS zona_nombre,
    cc.name AS community_name,
    cs.name AS sector_name,
    cper.name AS responsable,
    cper.dni
   FROM core_productionunit cp
     JOIN core_community cc ON cp.community_id = cc.id
     JOIN core_sector cs ON cp.sector_id = cs.id
     JOIN core_zone cz ON cp.zone_id = cz.id
     JOIN core_person cper ON cp.person_responsable_id = cper.id;