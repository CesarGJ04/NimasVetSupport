SELECT 
    vdw.visited_at AS fecha_visita,
    cz.name AS zona,
    cc.name AS comunidad,
    cs.name AS sector,
    cper.name AS up_responsable,
    vdw.up_member_name AS up_integrante,
    vdw.employ_specialist AS personal_especialista,
    vdw.employ_responsable AS personal_responsable,
    ca.name AS actividad,
	vdw.v_race AS Vacunos_raza,
	vdw.v_dewormed AS Vacunos_desparacitados,
	vdw.v_no_dewormed AS Vacunos_no_desparacitados,
	vdw.v_total AS Total_vacunos,
	vdw.o_race AS Ovinos_raza,
	vdw.o_dewormed AS Ovinos_desparasitados,
	vdw.o_no_dewormed AS Ovinos_no_desparasitados,
	vdw.o_total AS Total_ovinos,
	vdw.a_race AS Alpacas_raza,
	vdw.a_dewormed AS Alpacas_desparacitadas,
	vdw.a_no_dewormed AS Alpacas_no_desparacitadas,
	vdw.a_total AS Total_alpacas,
	vdw.l_race AS Llamas_raza,
	vdw.l_dewormed AS Llamas_desparacitadas,
	vdw.l_no_dewormed AS Llamas_no_desparacitadas,
	vdw.l_total AS Total_llamas,
	vdw.c_total AS Total_canes,
	vdw.total
FROM core_visitanimaldeworming vdw
JOIN core_productionunit cp 
    ON vdw.production_unit_id = cp.id
JOIN core_community cc 
    ON cp.community_id = cc.id
JOIN core_sector cs 
    ON cp.sector_id = cs.id
JOIN core_zone cz 
    ON cp.zone_id = cz.id
JOIN core_person cper 
    ON cp.person_responsable_id = cper.id
JOIN core_activity ca 
    ON vdw.activity_id = ca.id
ORDER BY vdw.visited_at DESC;