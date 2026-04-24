CREATE OR REPLACE VIEW public.vw_reportevacunos
 AS
 SELECT cvvh.visited_at,
    cz.name AS zona,
    cc.name AS comunidad,
    cs.name AS sector,
    cper.name AS up_responsable,
    cvvh.employ_specialist AS personal_especialista,
    cvvh.employ_responsable AS persona_responsable,
    ca.name AS actividad,
    cvvh.bull_name,
    cvvh.bull_race,
    cvvh.pajilla_type,
    cvvh.pajilla_origin,
    cvvh.pajillas_number,
    cvvh.cow_name,
    cvvh.cow_race,
    cvvh.service_number,
    cvvh.pregnant,
    cvvh.empty,
    cvvh.birthday,
    cvvh.earring_number,
    cvvh.baby_name,
    cvvh.male,
    cvvh.female,
    cvvh.death,
    cvvh.baby_bull_name,
    cvvh.baby_cow_name,
    cvvh.female_attendance,
    cvvh.male_attendance,
    cvvh.technical_assistance_attendance,
    cvvh.vacunos_number
   FROM core_productionunit cp
     JOIN core_community cc ON cp.community_id = cc.id
     JOIN core_sector cs ON cp.sector_id = cs.id
     JOIN core_zone cz ON cp.zone_id = cz.id
     JOIN core_visitgeneticimprovementvacuno cvvh ON cp.id = cvvh.production_unit_id
     JOIN core_activity ca ON cvvh.activity_id = ca.id
     JOIN core_person cper ON cp.person_responsable_id = cper.id;
