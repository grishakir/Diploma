import json
import

def create_docker_compose(init_config):
    config = json.loads(init_config)

    generation_modules = config['config']['traffic_generator']['generation_modules']
    attack_tester = config['config']['traffic_generator']['attack_tester']
    attack_address = config['config']['attack_address']['ip_address']

    compose_config = {
        'version': '3.8',
        'services': {
            'router': {
                'build': {
                    'context': '.',
                    'dockerfile': 'router'
                },
                'container_name': 'router',
                'cap_add': ['NET_ADMIN'],
                'networks': ['my_network'],
                'volumes': ['./data:/data']
            },
        },
        'networks': {
            'my_network': {
                'driver': 'bridge'
            }
        }
    }

    if attack_tester:
        compose_config['services']['attack_tester'] = {
            'build': {
                'context': '.',
                'dockerfile': 'attack'
            },
            'container_name': 'attack_tester',
            'networks': ['my_network'],
            'environment': {
                'ATTACK_ADDRESS': attack_address
            }
        }

    for i in range(1, generation_modules + 1):
        service_name = f'traffic_generator_{i}'
        compose_config['services'][service_name] = {
            'build': {
                'context': '.',
                'dockerfile': 'container'
            },
            'networks': ['my_network']
        }

    with open('docker-compose.yml', 'w') as file:
        yaml.dump(compose_config, file, default_flow_style=False)

if __name__ == "__main__":
    config_file = open('./config/main.json', 'r')
    init_config = config_file.readlines()
    create_docker_compose(init_config)
    
