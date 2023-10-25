import whois

def domain_info(domain_name):
    try:
        domain = whois.whois(domain_name)
        print("Domain Name: ", domain.domain_name)
        print("Registrar: ", domain.registrar)
        print("Creation Date: ", domain.creation_date)
        print("Expiration Date: ", domain.expiration_date)
        print("Name Servers: ", domain.name_servers)
        print("Status: ", domain.status)
        print("Updated Date: ", domain.updated_date)
    except Exception as e:
        print("Erro ao obter informações do domínio:", e)

if __name__ == "__main__":
    domain_name = input("Informe o nome de domínio (exemplo.com): ")
    domain_info(domain_name)
