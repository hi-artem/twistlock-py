# coding: utf-8

"""
    Prisma Cloud Compute API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 21.04.439
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.coderepos_scan_result import CodereposScanResult  # noqa: E501
from openapi_client.rest import ApiException

class TestCodereposScanResult(unittest.TestCase):
    """CodereposScanResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CodereposScanResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.coderepos_scan_result.CodereposScanResult()  # noqa: E501
        if include_optional :
            return CodereposScanResult(
                id = '', 
                collections = [
                    ''
                    ], 
                compliance_risk_score = 1.337, 
                files = [
                    openapi_client.models.coderepos/manifest_file.coderepos.ManifestFile(
                        dependencies = [
                            openapi_client.models.coderepos/pkg_dependency.coderepos.PkgDependency(
                                dev_dependency = True, 
                                last_resolved = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                license_severity = '', 
                                licenses = [
                                    '[\"0BSD\",\"AAL\",\"ADSL\",\"AFL-1.1\",\"AFL-1.2\",\"AFL-2.0\",\"AFL-2.1\",\"AFL-3.0\",\"AGPL-1.0\",\"AGPL-1.0-only\",\"AGPL-1.0-or-later\",\"AGPL-3.0\",\"AGPL-3.0-only\",\"AGPL-3.0-or-later\",\"AMDPLPA\",\"AML\",\"AMPAS\",\"ANTLR-PD\",\"ANTLR-PD-fallback\",\"APAFML\",\"APL-1.0\",\"APSL-1.0\",\"APSL-1.1\",\"APSL-1.2\",\"APSL-2.0\",\"Abstyles\",\"Adobe-2006\",\"Adobe-Glyph\",\"Afmparse\",\"Aladdin\",\"Apache-1.0\",\"Apache-1.1\",\"Apache-2.0\",\"Artistic-1.0\",\"Artistic-1.0-Perl\",\"Artistic-1.0-cl8\",\"Artistic-2.0\",\"BSD-1-Clause\",\"BSD-2-Clause\",\"BSD-2-Clause-FreeBSD\",\"BSD-2-Clause-NetBSD\",\"BSD-2-Clause-Patent\",\"BSD-2-Clause-Views\",\"BSD-3-Clause\",\"BSD-3-Clause-Attribution\",\"BSD-3-Clause-Clear\",\"BSD-3-Clause-LBNL\",\"BSD-3-Clause-No-Nuclear-License\",\"BSD-3-Clause-No-Nuclear-License-2014\",\"BSD-3-Clause-No-Nuclear-Warranty\",\"BSD-3-Clause-Open-MPI\",\"BSD-4-Clause\",\"BSD-4-Clause-UC\",\"BSD-Protection\",\"BSD-Source-Code\",\"BSL-1.0\",\"BUSL-1.1\",\"Bahyph\",\"Barr\",\"Beerware\",\"BitTorrent-1.0\",\"BitTorrent-1.1\",\"BlueOak-1.0.0\",\"Borceux\",\"CAL-1.0\",\"CAL-1.0-Combined-Work-Exception\",\"CATOSL-1.1\",\"CC-BY-1.0\",\"CC-BY-2.0\",\"CC-BY-2.5\",\"CC-BY-3.0\",\"CC-BY-3.0-AT\",\"CC-BY-3.0-US\",\"CC-BY-4.0\",\"CC-BY-NC-1.0\",\"CC-BY-NC-2.0\",\"CC-BY-NC-2.5\",\"CC-BY-NC-3.0\",\"CC-BY-NC-4.0\",\"CC-BY-NC-ND-1.0\",\"CC-BY-NC-ND-2.0\",\"CC-BY-NC-ND-2.5\",\"CC-BY-NC-ND-3.0\",\"CC-BY-NC-ND-3.0-IGO\",\"CC-BY-NC-ND-4.0\",\"CC-BY-NC-SA-1.0\",\"CC-BY-NC-SA-2.0\",\"CC-BY-NC-SA-2.5\",\"CC-BY-NC-SA-3.0\",\"CC-BY-NC-SA-4.0\",\"CC-BY-ND-1.0\",\"CC-BY-ND-2.0\",\"CC-BY-ND-2.5\",\"CC-BY-ND-3.0\",\"CC-BY-ND-4.0\",\"CC-BY-SA-1.0\",\"CC-BY-SA-2.0\",\"CC-BY-SA-2.0-UK\",\"CC-BY-SA-2.5\",\"CC-BY-SA-3.0\",\"CC-BY-SA-3.0-AT\",\"CC-BY-SA-4.0\",\"CC-PDDC\",\"CC0-1.0\",\"CDDL-1.0\",\"CDDL-1.1\",\"CDLA-Permissive-1.0\",\"CDLA-Sharing-1.0\",\"CECILL-1.0\",\"CECILL-1.1\",\"CECILL-2.0\",\"CECILL-2.1\",\"CECILL-B\",\"CECILL-C\",\"CERN-OHL-1.1\",\"CERN-OHL-1.2\",\"CERN-OHL-P-2.0\",\"CERN-OHL-S-2.0\",\"CERN-OHL-W-2.0\",\"CNRI-Jython\",\"CNRI-Python\",\"CNRI-Python-GPL-Compatible\",\"CPAL-1.0\",\"CPL-1.0\",\"CPOL-1.02\",\"CUA-OPL-1.0\",\"Caldera\",\"ClArtistic\",\"Condor-1.1\",\"Crossword\",\"CrystalStacker\",\"Cube\",\"D-FSL-1.0\",\"DOC\",\"DSDP\",\"Dotseqn\",\"ECL-1.0\",\"ECL-2.0\",\"EFL-1.0\",\"EFL-2.0\",\"EPICS\",\"EPL-1.0\",\"EPL-2.0\",\"EUDatagrid\",\"EUPL-1.0\",\"EUPL-1.1\",\"EUPL-1.2\",\"Entessa\",\"ErlPL-1.1\",\"Eurosym\",\"FSFAP\",\"FSFUL\",\"FSFULLR\",\"FTL\",\"Fair\",\"Frameworx-1.0\",\"FreeImage\",\"GFDL-1.1\",\"GFDL-1.1-invariants-only\",\"GFDL-1.1-invariants-or-later\",\"GFDL-1.1-no-invariants-only\",\"GFDL-1.1-no-invariants-or-later\",\"GFDL-1.1-only\",\"GFDL-1.1-or-later\",\"GFDL-1.2\",\"GFDL-1.2-invariants-only\",\"GFDL-1.2-invariants-or-later\",\"GFDL-1.2-no-invariants-only\",\"GFDL-1.2-no-invariants-or-later\",\"GFDL-1.2-only\",\"GFDL-1.2-or-later\",\"GFDL-1.3\",\"GFDL-1.3-invariants-only\",\"GFDL-1.3-invariants-or-later\",\"GFDL-1.3-no-invariants-only\",\"GFDL-1.3-no-invariants-or-later\",\"GFDL-1.3-only\",\"GFDL-1.3-or-later\",\"GL2PS\",\"GLWTPL\",\"GPL-1.0\",\"GPL-1.0+\",\"GPL-1.0-only\",\"GPL-1.0-or-later\",\"GPL-2.0\",\"GPL-2.0+\",\"GPL-2.0-only\",\"GPL-2.0-or-later\",\"GPL-2.0-with-GCC-exception\",\"GPL-2.0-with-autoconf-exception\",\"GPL-2.0-with-bison-exception\",\"GPL-2.0-with-classpath-exception\",\"GPL-2.0-with-font-exception\",\"GPL-3.0\",\"GPL-3.0+\",\"GPL-3.0-only\",\"GPL-3.0-or-later\",\"GPL-3.0-with-GCC-exception\",\"GPL-3.0-with-autoconf-exception\",\"Giftware\",\"Glide\",\"Glulxe\",\"HPND\",\"HPND-sell-variant\",\"HTMLTIDY\",\"HaskellReport\",\"Hippocratic-2.1\",\"IBM-pibs\",\"ICU\",\"IJG\",\"IPA\",\"IPL-1.0\",\"ISC\",\"ImageMagick\",\"Imlib2\",\"Info-ZIP\",\"Intel\",\"Intel-ACPI\",\"Interbase-1.0\",\"JPNIC\",\"JSON\",\"JasPer-2.0\",\"LAL-1.2\",\"LAL-1.3\",\"LGPL-2.0\",\"LGPL-2.0+\",\"LGPL-2.0-only\",\"LGPL-2.0-or-later\",\"LGPL-2.1\",\"LGPL-2.1+\",\"LGPL-2.1-only\",\"LGPL-2.1-or-later\",\"LGPL-3.0\",\"LGPL-3.0+\",\"LGPL-3.0-only\",\"LGPL-3.0-or-later\",\"LGPLLR\",\"LPL-1.0\",\"LPL-1.02\",\"LPPL-1.0\",\"LPPL-1.1\",\"LPPL-1.2\",\"LPPL-1.3a\",\"LPPL-1.3c\",\"Latex2e\",\"Leptonica\",\"LiLiQ-P-1.1\",\"LiLiQ-R-1.1\",\"LiLiQ-Rplus-1.1\",\"Libpng\",\"Linux-OpenIB\",\"MIT\",\"MIT-0\",\"MIT-CMU\",\"MIT-advertising\",\"MIT-enna\",\"MIT-feh\",\"MIT-open-group\",\"MITNFA\",\"MPL-1.0\",\"MPL-1.1\",\"MPL-2.0\",\"MPL-2.0-no-copyleft-exception\",\"MS-PL\",\"MS-RL\",\"MTLL\",\"MakeIndex\",\"MirOS\",\"Motosoto\",\"MulanPSL-1.0\",\"MulanPSL-2.0\",\"Multics\",\"Mup\",\"NASA-1.3\",\"NBPL-1.0\",\"NCGL-UK-2.0\",\"NCSA\",\"NGPL\",\"NIST-PD\",\"NIST-PD-fallback\",\"NLOD-1.0\",\"NLPL\",\"NOSL\",\"NPL-1.0\",\"NPL-1.1\",\"NPOSL-3.0\",\"NRL\",\"NTP\",\"NTP-0\",\"Naumen\",\"Net-SNMP\",\"NetCDF\",\"Newsletr\",\"Nokia\",\"Noweb\",\"Nunit\",\"O-UDA-1.0\",\"OCCT-PL\",\"OCLC-2.0\",\"ODC-By-1.0\",\"ODbL-1.0\",\"OFL-1.0\",\"OFL-1.0-RFN\",\"OFL-1.0-no-RFN\",\"OFL-1.1\",\"OFL-1.1-RFN\",\"OFL-1.1-no-RFN\",\"OGC-1.0\",\"OGL-Canada-2.0\",\"OGL-UK-1.0\",\"OGL-UK-2.0\",\"OGL-UK-3.0\",\"OGTSL\",\"OLDAP-1.1\",\"OLDAP-1.2\",\"OLDAP-1.3\",\"OLDAP-1.4\",\"OLDAP-2.0\",\"OLDAP-2.0.1\",\"OLDAP-2.1\",\"OLDAP-2.2\",\"OLDAP-2.2.1\",\"OLDAP-2.2.2\",\"OLDAP-2.3\",\"OLDAP-2.4\",\"OLDAP-2.5\",\"OLDAP-2.6\",\"OLDAP-2.7\",\"OLDAP-2.8\",\"OML\",\"OPL-1.0\",\"OSET-PL-2.1\",\"OSL-1.0\",\"OSL-1.1\",\"OSL-2.0\",\"OSL-2.1\",\"OSL-3.0\",\"OpenSSL\",\"PDDL-1.0\",\"PHP-3.0\",\"PHP-3.01\",\"PSF-2.0\",\"Parity-6.0.0\",\"Parity-7.0.0\",\"Plexus\",\"PolyForm-Noncommercial-1.0.0\",\"PolyForm-Small-Business-1.0.0\",\"PostgreSQL\",\"Python-2.0\",\"QPL-1.0\",\"Qhull\",\"RHeCos-1.1\",\"RPL-1.1\",\"RPL-1.5\",\"RPSL-1.0\",\"RSA-MD\",\"RSCPL\",\"Rdisc\",\"Ruby\",\"SAX-PD\",\"SCEA\",\"SGI-B-1.0\",\"SGI-B-1.1\",\"SGI-B-2.0\",\"SHL-0.5\",\"SHL-0.51\",\"SISSL\",\"SISSL-1.2\",\"SMLNJ\",\"SMPPL\",\"SNIA\",\"SPL-1.0\",\"SSH-OpenSSH\",\"SSH-short\",\"SSPL-1.0\",\"SWL\",\"Saxpath\",\"Sendmail\",\"Sendmail-8.23\",\"SimPL-2.0\",\"Sleepycat\",\"Spencer-86\",\"Spencer-94\",\"Spencer-99\",\"StandardML-NJ\",\"SugarCRM-1.1.3\",\"TAPR-OHL-1.0\",\"TCL\",\"TCP-wrappers\",\"TMate\",\"TORQUE-1.1\",\"TOSL\",\"TU-Berlin-1.0\",\"TU-Berlin-2.0\",\"UCL-1.0\",\"UPL-1.0\",\"Unicode-DFS-2015\",\"Unicode-DFS-2016\",\"Unicode-TOU\",\"Unlicense\",\"VOSTROM\",\"VSL-1.0\",\"Vim\",\"W3C\",\"W3C-19980720\",\"W3C-20150513\",\"WTFPL\",\"Watcom-1.0\",\"Wsuipa\",\"X11\",\"XFree86-1.1\",\"XSkat\",\"Xerox\",\"Xnet\",\"YPL-1.0\",\"YPL-1.1\",\"ZPL-1.1\",\"ZPL-2.0\",\"ZPL-2.1\",\"Zed\",\"Zend-2.0\",\"Zimbra-1.3\",\"Zimbra-1.4\",\"Zlib\",\"blessing\",\"bzip2-1.0.5\",\"bzip2-1.0.6\",\"copyleft-next-0.3.0\",\"copyleft-next-0.3.1\",\"curl\",\"diffmark\",\"dvipdfm\",\"eCos-2.0\",\"eGenix\",\"etalab-2.0\",\"gSOAP-1.3b\",\"gnuplot\",\"iMatix\",\"libpng-2.0\",\"libselinux-1.0\",\"libtiff\",\"mpich2\",\"psfrag\",\"psutils\",\"wxWindows\",\"xinetd\",\"xpp\",\"zlib-acknowledgement\"]'
                                    ], 
                                name = '', 
                                raw_requirement = '', 
                                unsupported = True, 
                                version = '', 
                                vulnerabilities = [
                                    openapi_client.models.vuln/vulnerability.vuln.Vulnerability(
                                        applicable_rules = [
                                            ''
                                            ], 
                                        binary_pkgs = [
                                            ''
                                            ], 
                                        block = True, 
                                        cause = '', 
                                        cri = True, 
                                        custom = True, 
                                        cve = '', 
                                        cvss = 1.337, 
                                        description = '', 
                                        discovered = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        exploit = '[\"\",\"exploit-db\",\"exploit-windows\"]', 
                                        fix_date = 56, 
                                        fix_link = '', 
                                        function_layer = '', 
                                        grace_period_days = 56, 
                                        id = 56, 
                                        layer_time = 56, 
                                        link = '', 
                                        package_name = '', 
                                        package_version = '', 
                                        published = 56, 
                                        risk_factors = {
                                            'key' : ''
                                            }, 
                                        severity = '', 
                                        status = '', 
                                        templates = [
                                            '[\"PCI\",\"HIPAA\",\"NIST SP 800-190\",\"GDPR\",\"DISA STIG\"]'
                                            ], 
                                        text = '', 
                                        title = '', 
                                        twistlock = True, 
                                        type = '[\"container\",\"image\",\"host_config\",\"daemon_config\",\"daemon_config_files\",\"security_operations\",\"k8s_master\",\"k8s_worker\",\"k8s_federation\",\"linux\",\"windows\",\"istio\",\"aws\",\"serverless\",\"custom\",\"docker_stig\"]', 
                                        vec_str = '', 
                                        vuln_tag_infos = [
                                            openapi_client.models.vuln/tag_info.vuln.TagInfo(
                                                comment = '', 
                                                name = '', )
                                            ], )
                                    ], )
                            ], 
                        distribution = openapi_client.models.vuln/distribution.vuln.Distribution(
                            critical = 56, 
                            high = 56, 
                            low = 56, 
                            medium = 56, 
                            total = 56, ), 
                        path = '', 
                        type = '[\"nodejs\",\"gem\",\"python\",\"jar\",\"package\",\"windows\",\"binary\",\"nuget\",\"go\"]', )
                    ], 
                _pass = True, 
                repository = openapi_client.models.coderepos/repository.coderepos.Repository(
                    build = '', 
                    default_branch = '', 
                    digest = '', 
                    full_name = '', 
                    job_name = '', 
                    name = '', 
                    owner = '', 
                    private = True, 
                    size = 56, ), 
                scan_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                type = '[\"github\",\"CI\"]', 
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                vuln_info = openapi_client.models.shared/image_info.shared.ImageInfo(
                    all_compliance = openapi_client.models.vuln/all_compliance.vuln.AllCompliance(
                        compliance = [
                            openapi_client.models.vuln/vulnerability.vuln.Vulnerability(
                                applicable_rules = [
                                    ''
                                    ], 
                                binary_pkgs = [
                                    ''
                                    ], 
                                block = True, 
                                cause = '', 
                                cri = True, 
                                custom = True, 
                                cve = '', 
                                cvss = 1.337, 
                                description = '', 
                                discovered = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                exploit = '[\"\",\"exploit-db\",\"exploit-windows\"]', 
                                fix_date = 56, 
                                fix_link = '', 
                                function_layer = '', 
                                grace_period_days = 56, 
                                id = 56, 
                                layer_time = 56, 
                                link = '', 
                                package_name = '', 
                                package_version = '', 
                                published = 56, 
                                risk_factors = {
                                    'key' : ''
                                    }, 
                                severity = '', 
                                status = '', 
                                templates = [
                                    '[\"PCI\",\"HIPAA\",\"NIST SP 800-190\",\"GDPR\",\"DISA STIG\"]'
                                    ], 
                                text = '', 
                                title = '', 
                                twistlock = True, 
                                type = '[\"container\",\"image\",\"host_config\",\"daemon_config\",\"daemon_config_files\",\"security_operations\",\"k8s_master\",\"k8s_worker\",\"k8s_federation\",\"linux\",\"windows\",\"istio\",\"aws\",\"serverless\",\"custom\",\"docker_stig\"]', 
                                vec_str = '', 
                                vuln_tag_infos = [
                                    openapi_client.models.vuln/tag_info.vuln.TagInfo(
                                        comment = '', 
                                        name = '', )
                                    ], )
                            ], 
                        enabled = True, ), 
                    applications = [
                        openapi_client.models.vuln/application.vuln.Application(
                            known_vulnerabilities = 56, 
                            layer_time = 56, 
                            name = '', 
                            path = '', 
                            version = '', )
                        ], 
                    base_image = '', 
                    binaries = [
                        openapi_client.models.shared/binary.shared.Binary(
                            altered = True, 
                            cve_count = 56, 
                            deps = [
                                ''
                                ], 
                            function_layer = '', 
                            md5 = '', 
                            missing_pkg = True, 
                            name = '', 
                            path = '', 
                            pkg_root_dir = '', 
                            services = [
                                ''
                                ], 
                            version = '', )
                        ], 
                    cloud_metadata = openapi_client.models.common/cloud_metadata.common.CloudMetadata(
                        account_id = '', 
                        image = '', 
                        labels = [
                            openapi_client.models.common/external_label.common.ExternalLabel(
                                key = '', 
                                source_name = '', 
                                source_type = '[\"namespace\",\"deployment\",\"aws\",\"azure\",\"gcp\"]', 
                                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                value = '', )
                            ], 
                        name = '', 
                        provider = '[\"aws\",\"azure\",\"gcp\",\"alibaba\",\"others\"]', 
                        region = '', 
                        resource_id = '', ), 
                    clusters = [
                        ''
                        ], 
                    compliance_distribution = openapi_client.models.vuln/distribution.vuln.Distribution(
                        critical = 56, 
                        high = 56, 
                        low = 56, 
                        medium = 56, 
                        total = 56, ), 
                    compliance_issues = [
                        openapi_client.models.vuln/vulnerability.vuln.Vulnerability(
                            block = True, 
                            cause = '', 
                            cri = True, 
                            custom = True, 
                            cve = '', 
                            cvss = 1.337, 
                            description = '', 
                            discovered = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            fix_date = 56, 
                            fix_link = '', 
                            function_layer = '', 
                            grace_period_days = 56, 
                            id = 56, 
                            layer_time = 56, 
                            link = '', 
                            package_name = '', 
                            package_version = '', 
                            published = 56, 
                            severity = '', 
                            status = '', 
                            text = '', 
                            title = '', 
                            twistlock = True, 
                            vec_str = '', )
                        ], 
                    compliance_issues_count = 56, 
                    compliance_risk_score = 1.337, 
                    creation_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    distro = '', 
                    ecs_cluster_name = '', 
                    external_labels = [
                        openapi_client.models.common/external_label.common.ExternalLabel(
                            key = '', 
                            source_name = '', 
                            timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            value = '', )
                        ], 
                    files = [
                        openapi_client.models.shared/file_details.shared.FileDetails(
                            md5 = '', 
                            path = '', 
                            sha1 = '', 
                            sha256 = '', )
                        ], 
                    first_scan_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    history = [
                        openapi_client.models.shared/image_history.shared.ImageHistory(
                            base_layer = True, 
                            created = 56, 
                            empty_layer = True, 
                            id = '', 
                            instruction = '', 
                            size_bytes = 56, 
                            tags = [
                                ''
                                ], 
                            vulnerabilities = [
                                openapi_client.models.vuln/vulnerability.vuln.Vulnerability(
                                    block = True, 
                                    cause = '', 
                                    cri = True, 
                                    custom = True, 
                                    cve = '', 
                                    cvss = 1.337, 
                                    description = '', 
                                    discovered = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                    fix_date = 56, 
                                    fix_link = '', 
                                    function_layer = '', 
                                    grace_period_days = 56, 
                                    id = 56, 
                                    layer_time = 56, 
                                    link = '', 
                                    package_name = '', 
                                    package_version = '', 
                                    published = 56, 
                                    severity = '', 
                                    status = '', 
                                    text = '', 
                                    title = '', 
                                    twistlock = True, 
                                    vec_str = '', )
                                ], )
                        ], 
                    host_devices = [
                        openapi_client.models.common/network_device_ip.common.NetworkDeviceIP(
                            ip = '', 
                            name = '', )
                        ], 
                    id = '', 
                    image = openapi_client.models.shared/image.shared.Image(
                        created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        entrypoint = [
                            ''
                            ], 
                        env = [
                            ''
                            ], 
                        healthcheck = True, 
                        id = '', 
                        layers = [
                            ''
                            ], 
                        os = '', 
                        repo_digest = [
                            ''
                            ], 
                        repo_tags = [
                            ''
                            ], 
                        user = '', 
                        working_dir = '', ), 
                    installed_products = openapi_client.models.shared/installed_products.shared.InstalledProducts(
                        apache = '', 
                        aws_cloud = True, 
                        crio = True, 
                        docker = '', 
                        docker_enterprise = True, 
                        has_package_manager = True, 
                        k8s_api_server = True, 
                        k8s_controller_manager = True, 
                        k8s_etcd = True, 
                        k8s_federation_api_server = True, 
                        k8s_federation_controller_manager = True, 
                        k8s_kubelet = True, 
                        k8s_proxy = True, 
                        k8s_scheduler = True, 
                        kubernetes = '', 
                        openshift = True, 
                        os_distro = '', 
                        serverless = True, 
                        swarm_manager = True, 
                        swarm_node = True, ), 
                    k8s_cluster_addr = '', 
                    labels = [
                        ''
                        ], 
                    layers = [
                        ''
                        ], 
                    missing_distro_vuln_coverage = True, 
                    namespaces = [
                        ''
                        ], 
                    os_distro = '', 
                    os_distro_release = '', 
                    os_distro_version = '', 
                    package_manager = True, 
                    packages = [
                        openapi_client.models.shared/packages.shared.Packages(
                            pkgs = [
                                openapi_client.models.shared/package.shared.Package(
                                    binary_idx = [
                                        56
                                        ], 
                                    cve_count = 56, 
                                    function_layer = '', 
                                    layer_time = 56, 
                                    license = '', 
                                    name = '', 
                                    path = '', 
                                    version = '', )
                                ], 
                            pkgs_type = '[\"nodejs\",\"gem\",\"python\",\"jar\",\"package\",\"windows\",\"binary\",\"nuget\",\"go\"]', )
                        ], 
                    registry_namespace = '', 
                    repo_digests = [
                        ''
                        ], 
                    repo_tag = openapi_client.models.shared/image_tag.shared.ImageTag(
                        digest = '', 
                        id = '', 
                        registry = '', 
                        repo = '', 
                        tag = '', ), 
                    risk_factors = {
                        'key' : ''
                        }, 
                    scan_version = '', 
                    startup_binaries = [
                        openapi_client.models.shared/binary.shared.Binary(
                            altered = True, 
                            cve_count = 56, 
                            function_layer = '', 
                            md5 = '', 
                            missing_pkg = True, 
                            name = '', 
                            path = '', 
                            pkg_root_dir = '', 
                            version = '', )
                        ], 
                    tags = [
                        openapi_client.models.shared/image_tag.shared.ImageTag(
                            digest = '', 
                            id = '', 
                            registry = '', 
                            repo = '', 
                            tag = '', )
                        ], 
                    top_layer = '', 
                    twistlock_image = True, 
                    vulnerabilities = [
                        openapi_client.models.vuln/vulnerability.vuln.Vulnerability(
                            block = True, 
                            cause = '', 
                            cri = True, 
                            custom = True, 
                            cve = '', 
                            cvss = 1.337, 
                            description = '', 
                            discovered = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            fix_date = 56, 
                            fix_link = '', 
                            function_layer = '', 
                            grace_period_days = 56, 
                            id = 56, 
                            layer_time = 56, 
                            link = '', 
                            package_name = '', 
                            package_version = '', 
                            published = 56, 
                            severity = '', 
                            status = '', 
                            text = '', 
                            title = '', 
                            twistlock = True, 
                            vec_str = '', )
                        ], 
                    vulnerabilities_count = 56, 
                    vulnerability_distribution = openapi_client.models.vuln/distribution.vuln.Distribution(
                        critical = 56, 
                        high = 56, 
                        low = 56, 
                        medium = 56, 
                        total = 56, ), 
                    vulnerability_risk_score = 1.337, ), 
                vulnerability_risk_score = 1.337, 
                vulnerable_files = 56
            )
        else :
            return CodereposScanResult(
        )

    def testCodereposScanResult(self):
        """Test CodereposScanResult"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
