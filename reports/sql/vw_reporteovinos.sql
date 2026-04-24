CREATE OR REPLACE VIEW public.vw_reporteovinos
 AS
 SELECT cvoh.visited_at,
    cz.name AS zona,
    cc.name AS comunidad,
    cs.name AS sector,
    cper.name AS up_responsable,
    cvoh.employ_specialist AS personal_especialista,
    cvoh.employ_responsable AS persona_responsable,
    ca.name AS actividad,
    cvoh.selected_ovines,
    cvoh.synchronized_ovines,
    cvoh.inseminated_sheeps_corriedale,
    cvoh.inseminated_sheeps_criollas,
    cvoh.pregnant,
    cvoh.empty,
    cvoh.not_evaluated,
    cvoh.baby_males,
    cvoh.baby_females,
    cvoh.baby_deaths,
    cvoh.course_female_attendance,
    cvoh.course_male_attendance,
    cvoh.technical_assistance_attendance,
    cvoh.ovinos_number
   FROM core_productionunit cp
     JOIN core_community cc ON cp.community_id = cc.id
     JOIN core_sector cs ON cp.sector_id = cs.id
     JOIN core_zone cz ON cp.zone_id = cz.id
     JOIN core_visitgeneticimprovementovino cvoh ON cp.id = cvoh.production_unit_id
     JOIN core_activity ca ON cvoh.activity_id = ca.id
     JOIN core_person cper ON cp.person_responsable_id = cper.id;