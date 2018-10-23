# Copyright IBM Corp, All Rights Reserved.
#
# SPDX-License-Identifier: Apache-2.0
#
import json
import os
import shutil

CLUSTER_NETWORK = "cello_net"

NETWORK_SIZE_FABRIC_PRE_V1 = [4, 6]
NETWORK_SIZE_FABRIC_V1 = [4]

# first port that can be assigned as cluster API
CLUSTER_PORT_START = int(os.getenv("CLUSTER_PORT_START", 7050))

# Fabric image related varible
# should be the same with scripts/worker_node/download_images.sh
HLF_VERSION = '1.0.5'
HLF_VERSION_1_1 = '1.1.0'
HLF_VERSION_1_2 = '1.2.0'

# vSphere requires this
ARCH = 'x86_64'
VERSION = '1.0.5'
BASEIMAGE_RELEASE = '0.3.2'
FABRIC_IMAGE_FULL = 'hyperledger/fabric-{}:{}-{}'
FABRIC_IMAGE_TAG = 'hyperledger/fabric-{}:{}'
FABRIC_IMAGE = 'hyperledger/fabric-{}'
FABRIC_IMAGES = ['peer', 'tools', 'orderer', 'ca', 'ccenv', 'kafka',
                 'zookeeper']
FABRIC_BASE_IMAGES = ['baseimage', 'baseos']

# explorer images
BLOCKCHAIN_EXPLORER_IMAGE = 'yeasy/blockchain-explorer'
BLOCKCHAIN_EXPLORER_TAG = '0.1.0-preview'

MYSQL_IMAGE = 'mysql'
MYSQL_TAG = '5.7'

# host status
HOST_STATUS = 'status'
HOST_STATUS_ACTIVE = 'active'
HOST_STATUS_PENDING = 'pending'

# number of port allocated to each cluster in case collision
CLUSTER_PORT_STEP = 100
CA_PORTS_UPPER_LIMIT = 10
ORDERER_PORTS_UPPER_LIMIT = 10

PEER_SERVICE_PORTS = {
    'rest': 7050,  # this is the reference starter for cluster port step
    'grpc': 7051,
    'cli': 7052,
    'event': 7053,
}

CA_SERVICE_PORTS = {
    'ecap': 7054,
    'ecaa': 7055,
    'tcap': 7056,
    'tcaa': 7057,
    'tlscap': 7058,
    'tlscaa': 7059,
}

ORDERER_SERVICE_PORTS = {
    'orderer': 7050
}

EXPLORER_PORTS = {
    'explorer': 8080
}

SERVICE_PORTS = dict(list(PEER_SERVICE_PORTS.items()) +
                     list(CA_SERVICE_PORTS.items()))

NETWORK_TYPE_FABRIC_PRE_V1 = 'fabric-0.6'  # TODO: deprecate 0.6 support soon
NETWORK_TYPE_FABRIC_V1 = 'fabric-1.0'
NETWORK_TYPE_FABRIC_V1_1 = 'fabric-1.1'
NETWORK_TYPE_FABRIC_V1_2 = 'fabric-1.2'
NETWORK_TYPES = [NETWORK_TYPE_FABRIC_V1, NETWORK_TYPE_FABRIC_V1_1,
                 NETWORK_TYPE_FABRIC_V1_2]
# only support fabric v1.x now

CONSENSUS_PLUGIN_NOOPS = 'noops'
CONSENSUS_PLUGIN_PBFT = 'pbft'
CONSENSUS_PLUGIN_SOLO = 'solo'
CONSENSUS_PLUGIN_KAFKA = 'kafka'

CONSENSUS_PLUGINS_FABRIC_V1 = [CONSENSUS_PLUGIN_SOLO, CONSENSUS_PLUGIN_KAFKA]
CONSENSUS_PLUGINS_FABRIC_PRE_V1 = [CONSENSUS_PLUGIN_NOOPS,
                                   CONSENSUS_PLUGIN_PBFT]
CONSENSUS_MODES_FABRIC_V1 = ['', '']

# CONSENSUS_MODES = ['classic', 'batch', 'sieve']  # pbft has various modes
CONSENSUS_MODE_BATCH = 'batch'
CONSENSUS_MODES = [CONSENSUS_MODE_BATCH]  # pbft has various modes

CONSENSUS_TYPES_FABRIC_PRE_V1 = [
    (CONSENSUS_PLUGIN_NOOPS, ''),
    (CONSENSUS_PLUGIN_PBFT, CONSENSUS_MODE_BATCH),
]

CONSENSUS_TYPES_FABRIC_V1 = [
    (CONSENSUS_PLUGIN_SOLO, ''),
    (CONSENSUS_PLUGIN_KAFKA, '')
]

WORKER_TYPE_DOCKER = 'docker'
WORKER_TYPE_SWARM = 'swarm'
WORKER_TYPE_K8S = 'kubernetes'
WORKER_TYPE_VSPHERE = 'vsphere'
WORKER_TYPES = [WORKER_TYPE_DOCKER, WORKER_TYPE_SWARM, WORKER_TYPE_K8S,
                WORKER_TYPE_VSPHERE]

# TODO: might deprecate as can use agent to collect log seperately
CLUSTER_LOG_TYPES = ['local']  # TODO: we may remove this option
CLUSTER_LOG_LEVEL = ['DEBUG', 'INFO', 'NOTICE', 'WARNING', 'ERROR',
                     'CRITICAL']

NETWORK_STATUS_CREATING = 'creating'  # just in-creation
NETWORK_STATUS_RUNNING = 'running'  # running now, waiting for health check
NETWORK_STATUS_DELETING = 'deleting'  # network is in deleting
NETWORK_STATUS_STOPPED = 'stopped'  # network is stopped
NETWORK_STATUS_UPDATING = 'updating'

K8S_CRED_TYPE = {
    'account': '0',
    'cert': '1',
    'config': '2'
}

# Vcenter and VirtualMachine Confs
VIRTUAL_MACHINE = 'vm'
VCENTER = 'vc'
VMUUID = 'vm_uuid'
VM_DEFAULT_HOSTNAME = "Cello"
VMMEMORY = 'memory'
VMCPU = 'vcpus'
VMNAME = 'vmname'
VMIP = 'ip'
VMNETMASK = 'netmask'
VMDNS = 'dns'
VMGATEWAY = 'gateway'
TEMPLATE = 'template'
VC_DATACENTER = 'vc_datacenter'
VC_CLUSTER = 'vc_cluster'
VC_DATASTORE = 'vc_datastore'
NETWORK = 'network'
NIC_DEVICE_ADDRESS_TYPE = 'assigned'
VCIP = 'address'
VCUSERNAME = 'username'
VCPWD = 'password'
VCPORT = 'port'
VC_DEFAULT_PORT = 443
VCTHREAD_NAME = "setupvm"
WORKER_API_PORT = 2375
DEFAULT_TIMEOUT = 300

NODETYPE_PEER = "peer"
NODETYPE_ORDERER = "orderer"
NODETYPE_CA = "ca"
NODETYPE_CLI = "cli"
ELEMENT_PVC="pvc"

EXTERNAL_SUB_MIX=31000
EXTERNAL_SUB_MAX=32000

def json_decode(jsonstr):
    try:
        json_object = json.loads(jsonstr)
    except json.decoder.JSONDecodeError as e:
        print(e)
        return jsonstr
    return json_object


def request_debug(request, logger):
    logger.debug("path={}, method={}".format(request.path, request.method))
    logger.debug("request args:")
    for k in request.args:
        logger.debug("Arg: {0}:{1}".format(k, request.args[k]))
    logger.debug("request form:")
    for k in request.form:
        logger.debug("Form: {0}:{1}".format(k, request.form[k]))
    logger.debug("request raw body data:")
    logger.debug(request.data)
    logger.debug(request.get_json(force=True, silent=True))


def request_get(request, key, default_value=None):
    if key in request.args:
        return request.args.get(key)
    elif key in request.form:
        return request.form.get(key)
    try:
        json_body = request.get_json(force=True, silent=True)
        if key in json_body:
            return json_body[key]
        else:
            return default_value
    except Exception:
        return default_value


def request_json_body(request, default_value={}):
    try:
        json_body = request.get_json(force=True, silent=True)
        return json_body
    except Exception:
        return default_value


def copytree(src, dst, symlinks=False, overwrite = None, ignore=None):
    '''
    :param src: the src is a dir
    :param dst: the dst is a dir
    :param symlinks: make a sysmlinks
    :param overwrite: overwrite if the dst is existed
    :param ignore:
    :return:
    '''
    names = os.listdir(src)
    if ignore is not None:
        ignored_names = ignore(src, names)
    else:
        ignored_names = set()

    # if overwrites is not None:
    #     overwrites =
    # else:

    if not os.path.isdir(dst):
        os.makedirs(dst)
    errors = []
    for name in names:
        if name in ignored_names:
            continue
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if os.path.islink(srcname):
                linkto = os.readlink(srcname)
                if symlinks:
                    # We can't just leave it to `copy_function` because legacy
                    # code with a custom `copy_function` may rely on copytree
                    # doing the right thing.
                    os.symlink(linkto, dstname)
                    shutil.copystat(srcname, dstname, follow_symlinks=not symlinks)
                else:
                    # ignore dangling symlink if the flag is on
                    if not os.path.exists(linkto):
                        continue
                    # otherwise let the copy occurs. copy2 will raise an error
                    if os.path.isdir(srcname):
                        copytree(srcname, dstname, symlinks, overwrite, ignore)
                    else:
                        shutil.copy2(srcname, dstname)
            elif os.path.isdir(srcname):
                copytree(srcname, dstname, symlinks, overwrite, ignore)
            else:
                if overwrite is not None:
                    if os.path.isfile(dstname):
                        overwrite(srcname, dstname)
                    else:
                        shutil.copy2(srcname, dstname)
                else:
                    # Will raise a SpecialFileError for unsupported file types
                    shutil.copy2(srcname, dstname)
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except shutil.Error as err:
            errors.extend (err.args[0])
        except OSError as why:
            errors.append ((srcname, dstname, str (why)))
    try:
        shutil.copystat(src, dst)
    except OSError as why:
        # Copying file access times may fail on Windows
        if getattr (why, 'winerror', None) is None:
            errors.append((src, dst, str (why)))
    if errors:
        raise shutil.Error(errors)
    return dst