from PyObjCTools.TestSupport import TestCase, min_os_level, onlyOn64Bit
import WebKit


class TestWKWebView(TestCase):
    @onlyOn64Bit
    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertResultIsBOOL(WebKit.WKWebView.isLoading)
        self.assertResultIsBOOL(WebKit.WKWebView.hasOnlySecureContent)
        self.assertResultIsBOOL(WebKit.WKWebView.canGoBack)
        self.assertResultIsBOOL(WebKit.WKWebView.canGoForward)
        self.assertResultIsBOOL(WebKit.WKWebView.allowsBackForwardNavigationGestures)
        self.assertArgIsBOOL(
            WebKit.WKWebView.setAllowsBackForwardNavigationGestures_, 0
        )
        self.assertResultIsBOOL(WebKit.WKWebView.allowsMagnification)
        self.assertArgIsBOOL(WebKit.WKWebView.setAllowsMagnification_, 0)
        self.assertArgIsBlock(
            WebKit.WKWebView.evaluateJavaScript_completionHandler_, 1, b"v@@"
        )

    @onlyOn64Bit
    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertResultIsBOOL(WebKit.WKWebView.allowsLinkPreview)
        self.assertArgIsBOOL(WebKit.WKWebView.setAllowsLinkPreview_, 0)

    @onlyOn64Bit
    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsBlock(
            WebKit.WKWebView.takeSnapshotWithConfiguration_completionHandler_, 1, b"v@@"
        )
        self.assertResultIsBOOL(WebKit.WKWebView.handlesURLScheme_)

    @onlyOn64Bit
    @min_os_level("10.15.4")
    def testMethods10_15_4(self):
        self.assertArgIsBlock(
            WebKit.WKWebView.createPDFWithConfiguration_completionHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            WebKit.WKWebView.createWebArchiveDataWithCompletionHandler_, 0, b"v@@"
        )
        self.assertArgIsBlock(
            WebKit.WKWebView.findString_withConfiguration_completionHandler_, 2, b"v@"
        )
