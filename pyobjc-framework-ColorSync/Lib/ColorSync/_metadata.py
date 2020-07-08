# This file is generated by objective.metadata
#
# Last update: Sat Jun 27 18:35:21 2020
#
# flake8: noqa

import objc, sys

if sys.maxsize > 2 ** 32:

    def sel32or64(a, b):
        return b


else:

    def sel32or64(a, b):
        return a


misc = {}
misc.update(
    {
        "ColorSyncMD5": objc.createStructType(
            "ColorSyncMD5", b"{_ColorSyncMD5=[16C]}", ["digest"]
        )
    }
)
constants = """$kCMMApplyTransformProcName@^{__CFString=}$kCMMCreateTransformPropertyProcName@^{__CFString=}$kCMMInitializeLinkProfileProcName@^{__CFString=}$kCMMInitializeTransformProcName@^{__CFString=}$kColorSyncACESCGLinearProfile@^{__CFString=}$kColorSyncAdobeRGB1998Profile@^{__CFString=}$kColorSyncBestQuality@^{__CFString=}$kColorSyncBlackPointCompensation@^{__CFString=}$kColorSyncCameraDeviceClass@^{__CFString=}$kColorSyncConversion1DLut@^{__CFString=}$kColorSyncConversion3DLut@^{__CFString=}$kColorSyncConversionBPC@^{__CFString=}$kColorSyncConversionChannelID@^{__CFString=}$kColorSyncConversionGridPoints@^{__CFString=}$kColorSyncConversionInpChan@^{__CFString=}$kColorSyncConversionMatrix@^{__CFString=}$kColorSyncConversionNDLut@^{__CFString=}$kColorSyncConversionOutChan@^{__CFString=}$kColorSyncConversionParamCurve0@^{__CFString=}$kColorSyncConversionParamCurve1@^{__CFString=}$kColorSyncConversionParamCurve2@^{__CFString=}$kColorSyncConversionParamCurve3@^{__CFString=}$kColorSyncConversionParamCurve4@^{__CFString=}$kColorSyncConvertQuality@^{__CFString=}$kColorSyncConvertThreadCount$kColorSyncConvertUseExtendedRange$kColorSyncConvertUseVectorUnit$kColorSyncCustomProfiles@^{__CFString=}$kColorSyncDCIP3Profile@^{__CFString=}$kColorSyncDeviceClass@^{__CFString=}$kColorSyncDeviceDefaultProfileID@^{__CFString=}$kColorSyncDeviceDescription@^{__CFString=}$kColorSyncDeviceDescriptions@^{__CFString=}$kColorSyncDeviceHostScope@^{__CFString=}$kColorSyncDeviceID@^{__CFString=}$kColorSyncDeviceModeDescription@^{__CFString=}$kColorSyncDeviceModeDescriptions@^{__CFString=}$kColorSyncDeviceProfileID@^{__CFString=}$kColorSyncDeviceProfileIsCurrent@^{__CFString=}$kColorSyncDeviceProfileIsDefault@^{__CFString=}$kColorSyncDeviceProfileIsFactory@^{__CFString=}$kColorSyncDeviceProfileURL@^{__CFString=}$kColorSyncDeviceProfilesNotification@^{__CFString=}$kColorSyncDeviceRegisteredNotification@^{__CFString=}$kColorSyncDeviceUnregisteredNotification@^{__CFString=}$kColorSyncDeviceUserScope@^{__CFString=}$kColorSyncDisplayDeviceClass@^{__CFString=}$kColorSyncDisplayDeviceProfilesNotification@^{__CFString=}$kColorSyncDisplayP3Profile@^{__CFString=}$kColorSyncDraftQuality@^{__CFString=}$kColorSyncExtendedRange@^{__CFString=}$kColorSyncFactoryProfiles@^{__CFString=}$kColorSyncFixedPointRange@^{__CFString=}$kColorSyncGenericCMYKProfile@^{__CFString=}$kColorSyncGenericGrayGamma22Profile@^{__CFString=}$kColorSyncGenericGrayProfile@^{__CFString=}$kColorSyncGenericLabProfile@^{__CFString=}$kColorSyncGenericRGBProfile@^{__CFString=}$kColorSyncGenericXYZProfile@^{__CFString=}$kColorSyncITUR2020Profile@^{__CFString=}$kColorSyncITUR709Profile@^{__CFString=}$kColorSyncNormalQuality@^{__CFString=}$kColorSyncPreferredCMM@^{__CFString=}$kColorSyncPrinterDeviceClass@^{__CFString=}$kColorSyncProfile@^{__CFString=}$kColorSyncProfileClass@^{__CFString=}$kColorSyncProfileColorSpace@^{__CFString=}$kColorSyncProfileComputerDomain@^{__CFString=}$kColorSyncProfileDescription@^{__CFString=}$kColorSyncProfileHeader@^{__CFString=}$kColorSyncProfileHostScope@^{__CFString=}$kColorSyncProfileMD5Digest@^{__CFString=}$kColorSyncProfilePCS@^{__CFString=}$kColorSyncProfileRepositoryChangeNotification@^{__CFString=}$kColorSyncProfileURL@^{__CFString=}$kColorSyncProfileUserDomain@^{__CFString=}$kColorSyncProfileUserScope@^{__CFString=}$kColorSyncROMMRGBProfile@^{__CFString=}$kColorSyncRegistrationUpdateWindowServer@^{__CFString=}$kColorSyncRenderingIntent@^{__CFString=}$kColorSyncRenderingIntentAbsolute@^{__CFString=}$kColorSyncRenderingIntentPerceptual@^{__CFString=}$kColorSyncRenderingIntentRelative@^{__CFString=}$kColorSyncRenderingIntentSaturation@^{__CFString=}$kColorSyncRenderingIntentUseProfileHeader@^{__CFString=}$kColorSyncSRGBProfile@^{__CFString=}$kColorSyncScannerDeviceClass@^{__CFString=}$kColorSyncSigAToB0Tag@^{__CFString=}$kColorSyncSigAToB1Tag@^{__CFString=}$kColorSyncSigAToB2Tag@^{__CFString=}$kColorSyncSigAbstractClass@^{__CFString=}$kColorSyncSigBToA0Tag@^{__CFString=}$kColorSyncSigBToA1Tag@^{__CFString=}$kColorSyncSigBToA2Tag@^{__CFString=}$kColorSyncSigBlueColorantTag@^{__CFString=}$kColorSyncSigBlueTRCTag@^{__CFString=}$kColorSyncSigCmykData@^{__CFString=}$kColorSyncSigColorSpaceClass@^{__CFString=}$kColorSyncSigCopyrightTag@^{__CFString=}$kColorSyncSigDeviceMfgDescTag@^{__CFString=}$kColorSyncSigDeviceModelDescTag@^{__CFString=}$kColorSyncSigDisplayClass@^{__CFString=}$kColorSyncSigGamutTag@^{__CFString=}$kColorSyncSigGrayData@^{__CFString=}$kColorSyncSigGrayTRCTag@^{__CFString=}$kColorSyncSigGreenColorantTag@^{__CFString=}$kColorSyncSigGreenTRCTag@^{__CFString=}$kColorSyncSigInputClass@^{__CFString=}$kColorSyncSigLabData@^{__CFString=}$kColorSyncSigLinkClass@^{__CFString=}$kColorSyncSigMediaBlackPointTag@^{__CFString=}$kColorSyncSigMediaWhitePointTag@^{__CFString=}$kColorSyncSigNamedColor2Tag@^{__CFString=}$kColorSyncSigNamedColorClass@^{__CFString=}$kColorSyncSigOutputClass@^{__CFString=}$kColorSyncSigPreview0Tag@^{__CFString=}$kColorSyncSigPreview1Tag@^{__CFString=}$kColorSyncSigPreview2Tag@^{__CFString=}$kColorSyncSigProfileDescriptionTag@^{__CFString=}$kColorSyncSigProfileSequenceDescTag@^{__CFString=}$kColorSyncSigRedColorantTag@^{__CFString=}$kColorSyncSigRedTRCTag@^{__CFString=}$kColorSyncSigRgbData@^{__CFString=}$kColorSyncSigTechnologyTag@^{__CFString=}$kColorSyncSigViewingCondDescTag@^{__CFString=}$kColorSyncSigViewingConditionsTag@^{__CFString=}$kColorSyncSigXYZData@^{__CFString=}$kColorSyncTranformInfo$kColorSyncTransformCodeFragmentMD5@^{__CFString=}$kColorSyncTransformCodeFragmentType@^{__CFString=}$kColorSyncTransformCreator@^{__CFString=}$kColorSyncTransformDeviceToDevice@^{__CFString=}$kColorSyncTransformDeviceToPCS@^{__CFString=}$kColorSyncTransformDstSpace@^{__CFString=}$kColorSyncTransformFullConversionData@^{__CFString=}$kColorSyncTransformGamutCheck@^{__CFString=}$kColorSyncTransformInfo@^{__CFString=}$kColorSyncTransformPCSToDevice@^{__CFString=}$kColorSyncTransformPCSToPCS@^{__CFString=}$kColorSyncTransformParametricConversionData@^{__CFString=}$kColorSyncTransformSimplifiedConversionData@^{__CFString=}$kColorSyncTransformSrcSpace@^{__CFString=}$kColorSyncTransformTag@^{__CFString=}$"""
enums = """$COLORSYNC_MD5_LENGTH@16$kColorSync10BitInteger@8$kColorSync16BitFloat@4$kColorSync16BitInteger@3$kColorSync1BitGamut@1$kColorSync32BitFloat@7$kColorSync32BitInteger@5$kColorSync32BitNamedColorIndex@6$kColorSync8BitInteger@2$kColorSyncAlphaFirst@4$kColorSyncAlphaInfoMask@31$kColorSyncAlphaLast@3$kColorSyncAlphaNone@0$kColorSyncAlphaNoneSkipFirst@6$kColorSyncAlphaNoneSkipLast@5$kColorSyncAlphaPremultipliedFirst@2$kColorSyncAlphaPremultipliedLast@1$kColorSyncByteOrder16Big@12288$kColorSyncByteOrder16Little@4096$kColorSyncByteOrder32Big@16384$kColorSyncByteOrder32Little@8192$kColorSyncByteOrderDefault@0$kColorSyncByteOrderMask@28672$"""
misc.update(
    {
        "COLORSYNC_PROFILE_INSTALL_ENTITLEMENT": b"com.apple.developer.ColorSync.profile.install"
    }
)
functions = {
    "ColorSyncProfileCopyDescriptionString": (
        b"^{__CFString=}^{ColorSyncProfile=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncCMMCopyLocalizedName": (
        b"^{__CFString=}^{ColorSyncCMM=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncProfileCreateLink": (
        b"^{ColorSyncProfile=}^{__CFArray=}^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncCreateCodeFragment": (
        b"@^{__CFArray=}^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncProfileCreateDisplayTransferTablesFromVCGT": (
        b"^{__CFData=}^{ColorSyncProfile=}n^Q",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {1: {"comment": "Unclear if this is correct"}},
        },
    ),
    "CGDisplayGetDisplayIDFromUUID": (b"I^{__CFUUID=}",),
    "ColorSyncProfileCreateDeviceProfile": (
        b"^{ColorSyncProfile=}^{__CFString=}^{__CFUUID=}@",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {2: {"comment": "CFTypeRef"}},
        },
    ),
    "ColorSyncProfileCopyHeader": (
        b"^{__CFData=}^{ColorSyncProfile=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncProfileCopyTagSignatures": (
        b"^{__CFArray=}^{ColorSyncProfile=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncCMMGetTypeID": (b"Q",),
    "ColorSyncProfileCreateWithURL": (
        b"^{ColorSyncProfile=}^{__CFURL=}^^{__CFError=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                1: {
                    "null_accepted": True,
                    "already_cfretained": True,
                    "type_modifier": "o",
                }
            },
        },
    ),
    "ColorSyncProfileVerify": (
        b"B^{ColorSyncProfile=}^^{__CFError=}^^{__CFError=}",
        "",
        {
            "arguments": {
                1: {
                    "null_accepted": True,
                    "already_cfretained": True,
                    "type_modifier": "o",
                },
                2: {
                    "null_accepted": True,
                    "already_cfretained": True,
                    "type_modifier": "o",
                },
            }
        },
    ),
    "ColorSyncTransformConvert": (
        b"B^{ColorSyncTransform=}QQ^vIIQ^vIIQ^{__CFDictionary=}",
        "",
        {
            "arguments": {
                3: {"type_modifier": "o", "c_array_of_variable_length": True},
                7: {"type_modifier": "n", "c_array_of_variable_length": True},
            }
        },
    ),
    "ColorSyncCMMCreate": (
        b"^{ColorSyncCMM=}^{__CFBundle=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncProfileCreateWithDisplayID": (
        b"^{ColorSyncProfile=}I",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncProfileCreateMutableCopy": (
        b"^{ColorSyncProfile=}^{ColorSyncProfile=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGDisplayCreateUUIDFromDisplayID": (
        b"^{__CFUUID=}I",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncProfileInstall": (
        b"B^{ColorSyncProfile=}^{__CFString=}^{__CFString=}^^{__CFError=}",
        "",
        {
            "arguments": {
                3: {
                    "null_accepted": True,
                    "already_cfretained": True,
                    "type_modifier": "o",
                }
            }
        },
    ),
    "ColorSyncProfileSetTag": (b"v^{ColorSyncProfile=}^{__CFString=}^{__CFData=}",),
    "ColorSyncTransformCreate": (
        b"^{ColorSyncTransform=}^{__CFArray=}^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncProfileCopyTag": (
        b"^{__CFData=}^{ColorSyncProfile=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncIterateDeviceProfiles": (
        b"v^?^v",
        "",
        {
            "arguments": {
                0: {
                    "callable": {
                        "retval": {"type": b"B"},
                        "arguments": {
                            0: {"type": b"^{__CFDictionary=}"},
                            1: {"type": b"^v"},
                        },
                    },
                    "callable_retained": False,
                }
            }
        },
    ),
    "ColorSyncProfileGetURL": (
        b"^{__CFURL=}^{ColorSyncProfile=}^^{__CFError=}",
        "",
        {
            "arguments": {
                1: {
                    "null_accepted": True,
                    "already_cfretained": True,
                    "type_modifier": "o",
                }
            }
        },
    ),
    "ColorSyncTransformSetProperty": (b"v^{ColorSyncTransform=}@@",),
    "ColorSyncUnregisterDevice": (b"B^{__CFString=}^{__CFUUID=}",),
    "ColorSyncDeviceCopyDeviceInfo": (
        b"^{__CFDictionary=}^{__CFString=}^{__CFUUID=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncProfileCreateMutable": (
        b"^{ColorSyncProfile=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncIterateInstalledProfiles": (
        b"v^?N^I^v^^{__CFError=}",
        "",
        {
            "arguments": {
                0: {
                    "callable": {
                        "retval": {"type": b"B"},
                        "arguments": {
                            0: {"type": b"^{__CFDictionary=}"},
                            1: {"type": b"^v"},
                        },
                    },
                    "callable_retained": False,
                },
                3: {
                    "null_accepted": True,
                    "already_cfretained": True,
                    "type_modifier": "o",
                },
            }
        },
    ),
    "ColorSyncProfileUninstall": (
        b"B^{ColorSyncProfile=}^^{__CFError=}",
        "",
        {
            "arguments": {
                1: {
                    "null_accepted": True,
                    "already_cfretained": True,
                    "type_modifier": "o",
                }
            }
        },
    ),
    "ColorSyncProfileCopyData": (
        b"^{__CFData=}^{ColorSyncProfile=}^^{__CFError=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                1: {
                    "null_accepted": True,
                    "already_cfretained": True,
                    "type_modifier": "o",
                }
            },
        },
    ),
    "ColorSyncIterateInstalledCMMs": (
        b"v^?^v",
        "",
        {
            "arguments": {
                0: {
                    "callable": {
                        "retval": {"type": b"B"},
                        "arguments": {
                            0: {"type": b"^{ColorSyncCMM=}"},
                            1: {"type": b"^v"},
                        },
                    },
                    "callable_retained": False,
                }
            }
        },
    ),
    "ColorSyncDeviceSetCustomProfiles": (
        b"B^{__CFString=}^{__CFUUID=}^{__CFDictionary=}",
    ),
    "ColorSyncCMMGetBundle": (b"^{__CFBundle=}^{ColorSyncCMM=}",),
    "ColorSyncProfileGetTypeID": (b"Q",),
    "ColorSyncProfileCreateWithName": (
        b"^{ColorSyncProfile=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncTransformGetTypeID": (b"Q",),
    "ColorSyncProfileGetDisplayTransferFormulaFromVCGT": (
        b"B^{ColorSyncProfile=}o^fo^fo^fo^fo^fo^fo^fo^fo^f",
    ),
    "ColorSyncRegisterDevice": (b"B^{__CFString=}^{__CFUUID=}^{__CFDictionary=}",),
    "ColorSyncProfileEstimateGammaWithDisplayID": (
        b"fi^^{__CFError=}",
        "",
        {
            "arguments": {
                1: {
                    "null_accepted": True,
                    "already_cfretained": True,
                    "type_modifier": "o",
                }
            }
        },
    ),
    "ColorSyncProfileGetMD5": (b"{_ColorSyncMD5=[16C]}^{ColorSyncProfile=}",),
    "ColorSyncProfileRemoveTag": (b"v^{ColorSyncProfile=}^{__CFString=}",),
    "ColorSyncProfileContainsTag": (
        b"B^{ColorSyncProfile=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncProfileEstimateGamma": (
        b"f^{ColorSyncProfile=}^^{__CFError=}",
        "",
        {
            "arguments": {
                1: {
                    "null_accepted": True,
                    "already_cfretained": True,
                    "type_modifier": "o",
                }
            }
        },
    ),
    "ColorSyncProfileCreate": (
        b"^{ColorSyncProfile=}^{__CFData=}^^{__CFError=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                1: {
                    "null_accepted": True,
                    "already_cfretained": True,
                    "type_modifier": "o",
                }
            },
        },
    ),
    "ColorSyncProfileSetHeader": (b"v^{ColorSyncProfile=}^{__CFData=}",),
    "ColorSyncTransformCopyProperty": (
        b"@^{ColorSyncTransform=}@^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "ColorSyncCMMCopyCMMIdentifier": (
        b"^{__CFString=}^{ColorSyncCMM=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
}
aliases = {
    "CSEXTERN_DESKTOP": "CSEXTERN",
    "ColorSyncMutableProfileRef": "ColorSyncProfileRef",
    "CS_UNAVAILABLE_PUBLIC_EMBEDDED": "CS_UNAVAILABLE_EMBEDDED",
}
cftypes = [
    ("ColorSyncCMMRef", b"^{ColorSyncCMM=}", "ColorSyncCMMGetTypeID", None),
    ("ColorSyncProfileRef", b"^{ColorSyncProfile=}", "ColorSyncProfileGetTypeID", None),
    (
        "ColorSyncTransformRef",
        b"^{ColorSyncTransform=}",
        "ColorSyncTransformGetTypeID",
        None,
    ),
]
expressions = {}

# END OF FILE
