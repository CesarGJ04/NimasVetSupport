CREATE OR REPLACE VIEW public.vw_SanidadAnimal
AS
SELECT 
    vah.visited_at AS fecha_visita,
    cz.name AS zona,
    cc.name AS comunidad,
    cs.name AS sector,
    cper.name AS up_responsable,
    vah.up_member_name AS up_integrante,
    vah.employ_specialist AS personal_especialista,
    vah.employ_responsable AS personal_responsable,
    ca.name AS actividad,
    so.name AS enfermedad_observacion,
    dia.name AS diagnostico,
    vah.vacunos,
    vah.ovinos,
    vah.alpacas,
    vah.llamas
FROM core_visitanimalhealth vah
JOIN core_productionunit cp 
    ON vah.production_unit_id = cp.id
JOIN core_community cc 
    ON cp.community_id = cc.id
JOIN core_sector cs 
    ON cp.sector_id = cs.id
JOIN core_zone cz 
    ON cp.zone_id = cz.id
JOIN core_person cper 
    ON cp.person_responsable_id = cper.id
JOIN core_activity ca 
    ON vah.activity_id = ca.id
LEFT JOIN core_sicknessobservation so 
    ON vah.sickness_observation_id = so.id
LEFT JOIN core_diagnostic dia 
    ON vah.diagnostic_id = dia.id
WHERE 
    vah.vacunos > 0
    OR vah.ovinos > 0
    OR vah.alpacas > 0
    OR vah.llamas > 0
ORDER BY vah.visited_at DESC;