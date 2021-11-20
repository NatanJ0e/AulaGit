import unittest
from time import sleep
from use_case.teste_topico.teste import log_in, url_projet, clic_button, cad_topc, cad_dest_nome, marc, close, get_array_elements, search, edit_topico

class testeEmpresa(unittest.TestCase):

    def test_logar_e_criar_topico(self):

        #login
        log_in('//input[@data-cg="field-user"]', 'natanael.ferreira', '//input[@data-cg="field-password"]', 'cg1501!@',
               '//button[@data-cg="btn-send"]')
        sleep(5)

        #mudança de url
        url_projet('http://10.50.0.26/app/topicos/#/')
        sleep(5)

        #cadastro
        cad_topc('//button[@data-cg="btn-create"]', '//select[@data-cg="field-gsu"]', '/html/body/app-root/div/div[2]/div/app-topicos-form/form/div[1]/div/select/option[1]', 'Informática - Desenvolvimento' )
        cad_dest_nome('//select[@data-cg="field-destino"]', '/html/body/app-root/div/div[2]/div/app-topicos-form/form/div[3]/div/select/option[1]','//input[@data-cg="field-nome"]', '852t')
        marc("no", "yes", "no", "no")

        #salvar cadastro
        clic_button('//button[@data-cg="btn-save"]')
        sleep(5)

        #pesquisar
        search('//input[@data-cg="field-pesquisar"]','852t', '//span[@class="ui-inputgroup-addon"]')

        #asserção
        elements = get_array_elements('body .ui-table .ui-table-tbody > tr')
        self.assertEqual(0, len(elements))

        #final
        close()

    def test_editar_cadastro_topico(self):
        # login
        log_in('//input[@data-cg="field-user"]', 'natanael.ferreira', '//input[@data-cg="field-password"]', 'cg1501!@',
               '//button[@data-cg="btn-send"]')
        sleep(5)

        # mudança de url
        url_projet('http://10.50.0.26/app/topicos/#/')
        sleep(5)

        # pesquisar
        search('//input[@data-cg="field-pesquisar"]', '852t', '//span[@class="ui-inputgroup-addon"]')

        #editar topico
        edit_topico('//button[@tooltipposition="left"]','//input[@data-cg="field-nome"]', '754t')

        #clicar em salvar
        clic_button('//button[@data-cg="btn-save"]')
        sleep(5)

        # pesquisar
        search('//input[@data-cg="field-pesquisar"]', '754t', '//span[@class="ui-inputgroup-addon"]')

        # asserção
        elements = get_array_elements('body .ui-table .ui-table-tbody > tr')
        self.assertEqual(0, len(elements))

        #fechar
        close()