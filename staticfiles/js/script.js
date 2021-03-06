// Usando query para pegar observar o campo id_nome_fluido1 quando for alterado
$("#id_nome_fluido1").on("change", function (){
	// Se o valor selecionado no campo for igual a duplotubo_agua esconde o campo id_Vazao1
	if ($("#id_nome_fluido1").val() == "Agua") {
		// Essa função "toogle()" esconde ou mostra um elemento dependendo do seu estado atual,
		// se esta escondido, mostra, se esta visivel, esconde
		$("#id_k1").prop('disabled', true);
		$("#id_cp1").prop('disabled', true);
		$("#id_Pr1").prop('disabled', true);
		$("#id_Densidade1").prop('disabled', true);
		$("#id_Viscos1").prop('disabled', true);
		$("#id_Viscos_tw1").prop('disabled', true);
	} 
	else if ($("#id_nome_fluido1").val() == "Butano") {
		// Essa função "toogle()" esconde ou mostra um elemento dependendo do seu estado atual,
		// se esta escondido, mostra, se esta visivel, esconde
		$("#id_k1").prop('disabled', true);
		$("#id_cp1").prop('disabled', true);
		$("#id_Pr1").prop('disabled', true);
		$("#id_Densidade1").prop('disabled', true);
		$("#id_Viscos1").prop('disabled', true);
		$("#id_Viscos_tw1").prop('disabled', true);
	}
	else if ($("#id_nome_fluido1").val() == "Co2") {
		// Essa função "toogle()" esconde ou mostra um elemento dependendo do seu estado atual,
		// se esta escondido, mostra, se esta visivel, esconde
		$("#id_k1").prop('disabled', true);
		$("#id_cp1").prop('disabled', true);
		$("#id_Pr1").prop('disabled', true);
		$("#id_Densidade1").prop('disabled', true);
		$("#id_Viscos1").prop('disabled', true);
		$("#id_Viscos_tw1").prop('disabled', true);
	}
	else if ($("#id_nome_fluido1").val() == "Metano") {
		// Essa função "toogle()" esconde ou mostra um elemento dependendo do seu estado atual,
		// se esta escondido, mostra, se esta visivel, esconde
		$("#id_k1").prop('disabled', true);
		$("#id_cp1").prop('disabled', true);
		$("#id_Pr1").prop('disabled', true);
		$("#id_Densidade1").prop('disabled', true);
		$("#id_Viscos1").prop('disabled', true);
		$("#id_Viscos_tw1").prop('disabled', true);
	}
	else if ($("#id_nome_fluido1").val() == "Pentano") {
		// Essa função "toogle()" esconde ou mostra um elemento dependendo do seu estado atual,
		// se esta escondido, mostra, se esta visivel, esconde
		$("#id_k1").prop('disabled', true);
		$("#id_cp1").prop('disabled', true);
		$("#id_Pr1").prop('disabled', true);
		$("#id_Densidade1").prop('disabled', true);
		$("#id_Viscos1").prop('disabled', true);
		$("#id_Viscos_tw1").prop('disabled', true);
	}
	else if ($("#id_nome_fluido1").val() == "RC318") {
		// Essa função "toogle()" esconde ou mostra um elemento dependendo do seu estado atual,
		// se esta escondido, mostra, se esta visivel, esconde
		$("#id_k1").prop('disabled', true);
		$("#id_cp1").prop('disabled', true);
		$("#id_Pr1").prop('disabled', true);
		$("#id_Densidade1").prop('disabled', true);
		$("#id_Viscos1").prop('disabled', true);
		$("#id_Viscos_tw1").prop('disabled', true);
	}
	else {
		$("#id_k1").prop('disabled', false);
		$("#id_cp1").prop('disabled', false);
		$("#id_Pr1").prop('disabled', false);
		$("#id_Densidade1").prop('disabled', false);
		$("#id_Viscos1").prop('disabled', false);
		$("#id_Viscos_tw1").prop('disabled', false);

	};
});

$("#id_nome_fluido2").on("change", function (){
	// Se o valor selecionado no campo for igual a duplotubo_agua esconde o campo id_Vazao1
	if ($("#id_nome_fluido2").val() == "Agua") {
		// Essa função "toogle()" esconde ou mostra um elemento dependendo do seu estado atual,
		// se esta escondido, mostra, se esta visivel, esconde
		$("#id_k2").prop('disabled', true);
		$("#id_cp2").prop('disabled', true);
		$("#id_Pr2").prop('disabled', true);
		$("#id_Densidade2").prop('disabled', true);
		$("#id_Viscos2").prop('disabled', true);
		$("#id_Viscos_tw2").prop('disabled', true);
	} 

	else if ($("#id_nome_fluido2").val() == "Butano") {
		// Essa função "toogle()" esconde ou mostra um elemento dependendo do seu estado atual,
		// se esta escondido, mostra, se esta visivel, esconde
		$("#id_k2").prop('disabled', true);
		$("#id_cp2").prop('disabled', true);
		$("#id_Pr2").prop('disabled', true);
		$("#id_Densidade2").prop('disabled', true);
		$("#id_Viscos2").prop('disabled', true);
		$("#id_Viscos_tw2").prop('disabled', true);
	}

		else if ($("#id_nome_fluido2").val() == "Co2") {
		// Essa função "toogle()" esconde ou mostra um elemento dependendo do seu estado atual,
		// se esta escondido, mostra, se esta visivel, esconde
		$("#id_k2").prop('disabled', true);
		$("#id_cp2").prop('disabled', true);
		$("#id_Pr2").prop('disabled', true);
		$("#id_Densidade1").prop('disabled', true);
		$("#id_Viscos2").prop('disabled', true);
		$("#id_Viscos_tw2").prop('disabled', true);
	}
	else if ($("#id_nome_fluido2").val() == "Metano") {
		// Essa função "toogle()" esconde ou mostra um elemento dependendo do seu estado atual,
		// se esta escondido, mostra, se esta visivel, esconde
		$("#id_k2").prop('disabled', true);
		$("#id_cp2").prop('disabled', true);
		$("#id_Pr2").prop('disabled', true);
		$("#id_Densidade2").prop('disabled', true);
		$("#id_Viscos2").prop('disabled', true);
		$("#id_Viscos_tw2").prop('disabled', true);
	}
	else if ($("#id_nome_fluido2").val() == "Pentano") {
		// Essa função "toogle()" esconde ou mostra um elemento dependendo do seu estado atual,
		// se esta escondido, mostra, se esta visivel, esconde
		$("#id_k2").prop('disabled', true);
		$("#id_cp2").prop('disabled', true);
		$("#id_Pr2").prop('disabled', true);
		$("#id_Densidade2").prop('disabled', true);
		$("#id_Viscos2").prop('disabled', true);
		$("#id_Viscos_tw2").prop('disabled', true);
	}
	else if ($("#id_nome_fluido2").val() == "RC318") {
		// Essa função "toogle()" esconde ou mostra um elemento dependendo do seu estado atual,
		// se esta escondido, mostra, se esta visivel, esconde
		$("#id_k2").prop('disabled', true);
		$("#id_cp2").prop('disabled', true);
		$("#id_Pr2").prop('disabled', true);
		$("#id_Densidade2").prop('disabled', true);
		$("#id_Viscos2").prop('disabled', true);
		$("#id_Viscos_tw2").prop('disabled', true);
	}

	else {
		$("#id_k2").prop('disabled', false);
		$("#id_cp2").prop('disabled', false);
		$("#id_Pr2").prop('disabled', false);
		$("#id_Densidade2").prop('disabled', false);
		$("#id_Viscos2").prop('disabled', false);
		$("#id_Viscos_tw2").prop('disabled', false);

	};
});








