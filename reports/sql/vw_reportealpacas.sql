CREATE OR REPLACE VIEW public.vw_reportealpacas AS
            SELECT cz.name AS zona,
                cc.name AS comunity_name,
                cs.name AS sector_name,
                cper.name AS up_responsable,
                cvah.employ_specialist AS personal_especialista,
                cvah.employ_responsable AS persona_responsable,
                ca.name AS actividad,
                cvah.visited_at,
                cvah.hato_number,
                cvah.hato_babies_number,
                cvah.hato_mothers_number,
                cvah.hato_males_number,
                cvah.female_alpaca_earring_number,
                cvah.female_alpaca_race,
                cvah.female_alpaca_color,
                cvah.female_alpaca_age,
                cvah.female_alpaca_category,
                cvah.female_alpaca_total_score,
                cvah.empadre_date,
                cvah.alpacas_empadradas,
                cvah.alpacas_empadradas_number,
                cvah.male_empadre_number,
                cvah.second_service_date,
                cvah.second_service_male_number,
                cvah.pregnant,
                cvah.empty,
                cvah.baby_birthday,
                cvah.baby_earring_number,
                cvah.female_baby,
                cvah.male_baby,
                cvah.mortality_baby,
                cvah.mother_of_baby,
                cvah.father_of_baby,
                cvah.activity_id,
                cvah.production_unit_id,
                cvah.selected_alpacas_number,
                cvah.technical_assistance_attendance,
                cvah.training_female_attendance,
                cvah.training_male_attendance
            FROM core_productionunit cp
            JOIN core_community cc ON cp.community_id = cc.id
            JOIN core_sector cs ON cp.sector_id = cs.id
            JOIN core_zone cz ON cp.zone_id = cz.id
            JOIN core_visitgeneticimprovementalpaca cvah ON cp.id = cvah.production_unit_id
            JOIN core_activity ca ON cvah.activity_id = ca.id
            JOIN core_person cper ON cp.person_responsable_id = cper.id;